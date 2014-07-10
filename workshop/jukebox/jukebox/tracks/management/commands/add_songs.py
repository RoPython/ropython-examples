from django.core.management.base import BaseCommand

from jukebox.foobar import Foobar
from jukebox.tracks.models import Artist, Track

class Command(BaseCommand):
    args = ''
    help = 'Add the songs from the foobar player'

    def handle(self, *args, **options):
        for artist, songs in Foobar().songs.items():
            artist, created = Artist.objects.get_or_create(name=artist)
            for track_name, tid in songs.items():
                Track.objects.create(
                    track_name=track_name, tid=tid, artist=artist)