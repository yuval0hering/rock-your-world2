
class Song:
    def __init__(self, song, singer):
        self.song = song
        self.singer = singer

    def to_json(self):
        return {"song": self.song, "singer": self.singer}