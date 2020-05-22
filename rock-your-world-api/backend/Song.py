class Song:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist

    def to_json(self):
        return {"song": self.song, "artist": self.artist}