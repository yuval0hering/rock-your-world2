import json
import os
import lyricsgenius
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from place import Place
from song import Song


def main():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "songs.json")
    with open(path, "r") as songs_json:
        song_list = json.load(songs_json)
    for s in song_list:
        song = get_song_lyrics(s['name'], s['artist'])
        song_title = song.title
        song_artist = song.artist
        lyrics = song.lyrics
        places = find_places_in_lyrics(lyrics)
        if places is not []:
            create_places_json(places, song_title, song_artist)


def get_song_lyrics(song_name, artist):
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    song = genius.search_song(song_name, artist)
    return song


def find_places_in_lyrics(lyrics):
    st = StanfordNERTagger(
        '/Users/yuvalhering/Desktop/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
        '/Users/yuvalhering/Desktop/stanford-ner-2018-10-16/stanford-ner.jar',
        encoding='utf-8')
    tokenized_text = word_tokenize(lyrics)
    classified_text = st.tag(tokenized_text)
    ner_places = []
    for classification in classified_text:
        if classification[1] == 'LOCATION':
            ner_places.append(classification[0])
    return list(set(ner_places))


def create_places_json(extracted_places, song_title, song_artist):
    places = []

    for new_place_name in extracted_places:
        exists = False
        for place in places:
            if place.name == new_place_name:
                place.add_song(song_title, song_artist)
                exists = True
                break
        if not exists:
            p = Place(new_place_name)
            p.add_song(song_title, song_artist)
            places.append(p)

    json_places = []

    for p in places:
        place_dict = p.to_json()
        json_places.append(place_dict)

    with open('places.json', 'w', encoding='utf-8') as places_file:
        json.dump(json_places, places_file, indent=2)


if __name__ == '__main__':
    main()
