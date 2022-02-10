def get_all_artists():
    from Core.music_structures.spotipy_data import SpotipyData
    return SpotipyData().artists


def get_all_album_name_by_artist_id(artist_id: str):
    from Core.music_structures.spotipy_data import SpotipyData
    for artist in SpotipyData().artists:
        if artist.id is artist_id:
            album_names = []
            for album in artist:
                album_names.append(album.name)
            return album_names
    return "artist id does not exist"
