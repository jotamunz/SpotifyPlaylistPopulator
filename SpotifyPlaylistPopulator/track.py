class Track:

    def __init__(self, name, id, artist):
        """
        :param name: (str) Track name
        :param id: (str) Spotify track id
        :param artist: (str) Track artist
        """
        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def create_spotify_uri_json(self):
        return {"uri": f"spotify:track:{self.id}"}

    def __str__(self):
        return self.name + " by " + self.artist
