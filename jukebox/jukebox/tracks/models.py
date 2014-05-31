from django.db import models
from django.contrib.auth.models import User
    
class Artist(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return "<Artist {}>".format(self.name)

    class Meta:
       db_table = 'artists'

class Track(models.Model):
    track_name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist)
    tid = models.IntegerField()

    def __repr__(self):
        return "<Track {} by {}; id {}>".format(
            self.track_name, self.artist.name, self.tid)

    class Meta:
       db_table = 'tracks'

class Vote(models.Model):
    user = models.ForeignKey(User, related_name="user_vote")
    track = models.ForeignKey(Track, related_name="track")
