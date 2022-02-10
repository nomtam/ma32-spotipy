def get_all_artists():
    from Core.music_structures.spotipy_data import SpotipyData
    return SpotipyData().artists


def get_all_album_name_by_artist_id(artist_id: str):
    import Monitoring.logger as logger
    from Core.music_structures.spotipy_data import SpotipyData
    from Monitoring.exceptions import ArtistIdDoesNotExistError
    logger.add_info("getting all albums by artist id")
    for artist in SpotipyData().artists:
        if artist.id == artist_id:
            album_names = []
            for album in artist.albums:
                album_names.append(album.name)
            return album_names
    logger.add_error(ArtistIdDoesNotExistError(artist_id))
    return "artist id does not exist"


def get_all_album_songs_by_album_id(album_id: str):
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.helpers import flatten_nested_list, remove_duplicates_from_list
    import Monitoring.logger as logger
    logger.add_info("getting all songs by album id: %s" % album_id)
    album_songs = list()
    for artist in SpotipyData().artists:
        if [track.name for album in artist.albums for track in album.tracks if album.id == album_id]:
            album_songs.append(
                [track.name for album in artist.albums for track in album.tracks if album.id == album_id])
    return remove_duplicates_from_list(flatten_nested_list(album_songs))


def get_all_artist_tracks_by_artist_id(artist_id: str):
    from Core.music_structures.spotipy_data import SpotipyData
    songs = []
    for artist in SpotipyData().artists:
        if artist.id == artist_id:
            songs = [track for album in artist.albums for track in album.tracks]
    return songs


def get_most_popular_artist_tracks_by_artist_id(artist_id: str):
    import Monitoring.configurator as config
    songs = get_all_artist_tracks_by_artist_id(artist_id)
    songs.sort(key=lambda track: track.popularity)
    return songs[:int(config.config_data['SEARCH_DATA']['POPULAR_SONGS'])]
