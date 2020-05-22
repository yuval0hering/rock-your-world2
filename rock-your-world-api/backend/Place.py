import geopy
from song import Song


class Place:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.__find_coordinates()

    def __find_coordinates(self):
        locator = geopy.Nominatim(user_agent="myGeocoder")
        location = locator.geocode(self.name)
        self.latitude = location.latitude
        self.longitude = location.longitude


    def place_dict(self):
        return self.__dict__

    def add_song(self, song_name, artist):
        self.songs.append(Song(song_name, artist))

    def to_json(self):
        songs_json = []
        for song in self.songs:
            songs_json.append(song.to_json())

        return {"name": self.name, "songs": songs_json, "latitude": self.latitude, "longitude": self.longitude}
