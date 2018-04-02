import os
from mpd import MPDClient


class MPD:

    def __init__(self):
        self.client = MPDClient()

    def _get_client(self):
        """
        Connects to mpd server and returns client
        :return:
        """
        client = self.client

        client.connect(os.environ.get("MPD_HOST", "localhost"), 6600)

        return client

    def get_playlist(self):
        client = self._get_client()
        playlist = client.playlistid()
        client.disconnect()
        return playlist

    def get_playlist_info(self):
        client = self._get_client()
        playlistinfo = client.playlistinfo()
        client.disconnect()
        return playlistinfo

    def set_playlist(self, playlist):
        """
        Clear and set new playlist
        :param playlist: array of radio urls
        :return:
        """
        client = self._get_client()
        client.clear()
        for uri in playlist:
            client.add(uri)
        client.disconnect()
        return True
