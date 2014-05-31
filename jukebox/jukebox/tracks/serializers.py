from rest_framework.serializers import ModelSerializer
from .models import Track, Artist

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track

    def to_native(self, obj):
        native = super().to_native(obj)
        native['artist'] = obj.artist.name
        return native

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist

    def to_native(self, obj):
        native = super().to_native(obj)        
        native['tracks'] = [
            TrackSerializer(track).data
            for track in obj.track_set.all()
        ]
        return native
        