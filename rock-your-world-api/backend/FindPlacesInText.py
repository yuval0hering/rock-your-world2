import json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from Place import Place


def find_places_in_lyrics(lyrics, song_title, song_artist):
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
    extracted_places = list(set(ner_places))

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


