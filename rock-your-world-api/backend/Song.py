class Song:
    def __init__(self, song, artist, lyrics, url):
        self.__type__ = 'Song'
        self.song = song
        self.artist = artist
        self.lyrics = lyrics
        self.url = url

    def to_json(self):
        return {"__type__": self.__type__, "song": self.song, "artist": self.artist, "lyrics": self.lyrics, "url": self.url}

    @staticmethod
    def as_song(dct):
        if '__type__' in dct and dct['__type__'] == 'Song':
            return Song(dct['song'], dct['artist'])
        return dct
