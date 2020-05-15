def tracklist(**kwargs):
    for musician, albums in kwargs.items():
        print(musician)
        for album, track in albums.items():
            print(f'ALBUM: {album} TRACK: {track}')
