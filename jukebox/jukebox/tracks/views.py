from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from jukebox.foobar import Foobar

from .serializers import TrackSerializer, ArtistSerializer
from .models import Artist, Track

class BaseJukebox:    
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ArtistList(generics.ListAPIView, BaseJukebox):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class Playlist(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class Song(generics.RetrieveAPIView,
           generics.UpdateAPIView):
    model = Track
    serializer_class = TrackSerializer

    def put(self, request, *args, **kwargs):
        track = self.get_object()
        Foobar().play_song(track.tid)
        return Response("Now playing song {}".format(track.track_name),
                        status=status.HTTP_200_OK)
