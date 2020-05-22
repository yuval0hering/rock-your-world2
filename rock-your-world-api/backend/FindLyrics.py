import lyricsgenius


def get_song_lyrics(song_name, artist):
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    song = genius.search_song(song_name, artist)
    return song

