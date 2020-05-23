import geopy
from song import Song


class Place:

    def __init__(self, name, songs=[], latitude=0, longitude=0):
        self.__type__ = 'Place'
        self.name = name
        self.songs = songs
        self.latitude = latitude
        self.longitude = longitude

    def find_coordinates(self):
        locator = geopy.Nominatim(user_agent="myGeocoder")
        location = locator.geocode(self.name)
        if location is not None:
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

        return {"__type__": self.__type__, "name": self.name, "songs": songs_json, "latitude": self.latitude, "longitude": self.longitude}

    @staticmethod
    def as_place(dct):
        if dct['__type__'] == 'Place':
            songs = Song.as_song(dct['songs'])
            return Place(dct['name'], songs, dct['latitude'], dct['longitude'])
        return dct
