import json
import os
import lyricsgenius
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from place import Place


def main():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "songs.json")
    places = []
    with open(path, "r") as songs_json:
        song_list = json.load(songs_json)
    for s in song_list:
        song = get_song_lyrics(s['name'], s['artist'])
        i = 0
        while i < 2:
            i += 1
            if song is None:
                song = get_song_lyrics(s['name'], s['artist'])
            else:
                break
        if song is not None:
            song_title = song.title
            song_artist = song.artist
            lyrics = song.lyrics
            extracted_places = find_places_in_lyrics(lyrics)
            if extracted_places is not []:
                places = create_places_list(places, extracted_places, song_title, song_artist)
    places_to_json(places)


def get_song_lyrics(song_name, artist):
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    song = genius.search_song(song_name, artist)
    return song


def find_places_in_lyrics(lyrics):
    st = StanfordNERTagger(
        '../stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
        '../stanford-ner-2018-10-16/stanford-ner.jar',
        encoding='utf-8')
    tokenized_text = word_tokenize(lyrics)
    classified_text = st.tag(tokenized_text)
    ner_places = []
    for classification in classified_text:
        if classification[1] == 'LOCATION':
            ner_places.append(classification[0].translate({ord('.'): None}))
    return list(set(ner_places))


def create_places_list(places, extracted_places, song_title, song_artist):

    for new_place_name in extracted_places:
        exists = False
        for place in places:
            if place.name == new_place_name:
                place.add_song(song_title, song_artist)
                exists = True
                break
        if not exists:
            p = Place(new_place_name, [])
            p.find_coordinates()
            if p.latitude != 0 or p.longitude != 0:
                p.add_song(song_title, song_artist)
                places.append(p)
    return places


def places_to_json(places):
    json_places = []

    for p in places:
        place_dict = p.to_json()
        json_places.append(place_dict)

    with open('places.json', 'w', encoding='utf-8') as places_file:
        json.dump(json_places, places_file, indent=2)


if __name__ == '__main__':
    main()
