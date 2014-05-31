from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .serializers import TrackSerializer, ArtistSerializer
from .models import Artist, Track

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class Playlist(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @action(permission_classes=(IsAdminUser, ))
    def post(self, request, *args, **kwargs):
        print(request)
