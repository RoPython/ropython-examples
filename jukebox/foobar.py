"""
Control foobar audio player through its COM
interface plugin.
"""
from collections import defaultdict     

import win32com.client
import pythoncom

FOOBAR_ID = "Foobar2000.Application.0.7"

class Foobar:
    @property
    def instance(self):
        try:
             return self._instance
        except AttributeError:
             pythoncom.CoInitialize()
             self._instance = win32com.client.Dispatch(FOOBAR_ID)
             return self._instance
 
    @property
    def songs(self):
         try:
             return self._songs
         except AttributeError:
             self._songs = defaultdict(dict)
             playlist = self.instance.Playlists.ActivePlaylist
             for index, track in enumerate(playlist.GetTracks("")):
                 artist = track.FormatTitle("%artist%")
                 title = track.FormatTitle("%title%")
                 self._songs[artist][title] = index  
             return self._songs

    @property
    def playing(self):
        return self.instance.Playback.IsPlaying

    def play(self):
        self.instance.Playback.Start(False)

    def stop(self):
        self.instance.Playback.Stop()

    def play_song(self, song_id):
        playlist = self.instance.Playlists.ActivePlaylist
        playlist.DoDefaultAction(song_id)
