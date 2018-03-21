from mpd import MPDClient


class MPD:

    def __init__(self):
        self.client = MPDClient()

    def _get_client(self):

        client = self.client

        client.connect("192.168.0.107", 6600)

        return client

    def get_playlist(self):
        client = self._get_client()
        playlist = client.playlist()
        client.disconnect()
        return playlist

    def get_playlist_info(self):
        client = self._get_client()
        playlistinfo = client.playlistinfo()
        client.disconnect()
        return playlistinfo
