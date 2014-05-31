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
    vote_count = models.IntegerField(default=0)    

    def __repr__(self):
        return "<Track {} by {}>".format(self.track_name, self.artist.name)

    class Meta:
       db_table = 'tracks'

class Vote(models.Model):
    user = models.ForeignKey(User, related_name="user_vote")
    track = models.ForeignKey(Track, related_name="track")
