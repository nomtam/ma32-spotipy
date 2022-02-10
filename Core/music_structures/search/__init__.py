def get_all_artists():
    from Core.music_structures.spotipy_data import SpotipyData
    return SpotipyData().artists
