import lyricsgenius


def main():
    genius = lyricsgenius.Genius('ifAv5R1fL3F6sMRXubPSueXJ3AlOe_gUu7MftBKJYR5dK8xMvw2_JCmgMc4ltmmi')
    artist = genius.search_artist("Billy Joel", max_songs=30)
    print()




if __name__ == '__main__':
    main()