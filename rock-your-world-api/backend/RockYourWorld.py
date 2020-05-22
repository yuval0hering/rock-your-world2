import json
import os
import FindLyrics


def main():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "songs.json")
    with open(path, "r") as songs_json:
        song_list = json.load(songs_json)
    for s in song_list:
        song = FindLyrics.get_song_lyrics(s['name'], s['artist'])
        song_title = song.title
        song_artist = song.artist
        lyrics = song.lyrics



if __name__ == '__main__':
    main()
