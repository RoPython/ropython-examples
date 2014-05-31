""" Models for the auth token. """

import uuid
import hmac
from hashlib import sha1

from django.db import models
from django.contrib.auth.models import User

class AuthToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    host = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="user", null=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = AuthToken.generate_key()
        return super(AuthToken, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        """ Generate a new unique key used 
        for tokens.
        """
        unique = uuid.uuid4()
        return hmac.new(unique.bytes, digestmod=sha1).hexdigest()

    def user_info(self):
        """ Used for serializing user information """
        return {
          "user_id": self.user.id,
          "username": self.user.username,
        }

    def __repr__(self):
        return ("<AuthToken; key={}, user={}>"
                .format(self.key, self.user.username))

    def __unicode__(self):
        return self.key

    __str__ = __unicode__
