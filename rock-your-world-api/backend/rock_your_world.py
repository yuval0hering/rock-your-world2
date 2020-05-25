import json
import os
import lyricsgenius
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from place import Place


def main():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "songs.json")
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    places = []
    with open(path, "r") as songs_json:
        song_list = json.load(songs_json)
    for s in song_list:
        song = get_song_lyrics(genius, s['name'], s['artist'])
        i = 0
        while i < 2:
            i += 1
            if song is None:
                song = get_song_lyrics(genius, s['name'], s['artist'])
            else:
                break
        if song is not None:
            extracted_places = find_places_in_lyrics(song.lyrics)
            if extracted_places is not []:
                places = create_places_list(places, extracted_places, song.title, song.artist, song.lyrics, song.url)
    places_to_json(places)


def get_song_lyrics(genius, song_name, artist):
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
    for i in range(0, len(classified_text) - 1):
        if classified_text[i][1] == 'LOCATION':
            if classified_text[i + 1][1] == 'LOCATION':
                ner_places.append(classified_text[i][0].translate({ord('.'): None}) + " " +
                                  classified_text[i + 1][0].translate({ord('.'): None}))
                i += 1
            else:
                ner_places.append(classified_text[i][0].translate({ord('.'): None}))
    copy_places = ner_places.copy()
    for place in ner_places:
        splitted = place.split()
        for word in splitted:
            first_ch = word[0]
            if not first_ch.isupper():
                copy_places.remove(place)
                break
    return list(set(copy_places))


def create_places_list(places, extracted_places, song_title, song_artist, song_lyrics, song_url):
    for new_place_name in extracted_places:
        exists = False
        for place in places:
            if place.name == new_place_name:
                place.add_song(song_title, song_artist, song_lyrics, song_url)
                exists = True
                break
        if not exists:
            p = Place(new_place_name, [])
            p.find_coordinates()
            if p.latitude != 0 or p.longitude != 0:
                p.add_song(song_title, song_artist, song_lyrics, song_url)
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
