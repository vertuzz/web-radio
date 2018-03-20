from mpd import MPDClient



class MPD:

    def __init__(self):
        self.client = self._get_client()

    def _get_client(self):

        client = MPDClient()

        client.connect("192.168.0.107", 6600)

        return client

    def get_playlist(self):
        return self.client.playlist()

    def get_playlist_info(self):
        return self.client.playlistinfo()