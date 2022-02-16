# CR: why in the init?
# CR: why are you importing in the methods?
# CR: if you would have saved the data in dicts no for would be needed here


def get_all_artists(username: str):
    from Core.users.data import UsersData
    import Monitoring.configurator as config
    from Core.music_structures.spotipy_data import SpotipyData
    # CR: config
    # CR: using the 'free' str makes it super coupled
    # CR: you can put the limiter in an other method
    return SpotipyData().artists[
           :int(config.config_data['SEARCH_DATA']['FREE_USER_MAX_RESULTS'])] if UsersData().get_user_permission_level(
        username) == 'free' else SpotipyData().artists


def get_all_album_name_by_artist_id(artist_id: str, username: str):
    import Monitoring.logger as logger
    from Core.users.data import UsersData
    from Core.music_structures.spotipy_data import SpotipyData
    import Monitoring.configurator as config
    from Monitoring.exceptions import ArtistIdDoesNotExistError
    # CR: better log: "{username} searched for albums by {artist_id}"
    logger.add_info("getting all albums by artist id")
    for artist in SpotipyData().artists:
        if artist.id == artist_id:
            album_names = []
            # CR: list comprehension
            for album in artist.albums:
                album_names.append(album.name)
            # CR: same for limiter as above
            return album_names[
                   :int(config.config_data['SEARCH_DATA'][
                            'FREE_USER_MAX_RESULTS'])] if UsersData().get_user_permission_level(
                username) == 'free' else album_names
    logger.add_error(ArtistIdDoesNotExistError(artist_id))
    # CR: why returning this? raise error or return empty
    return "artist id does not exist"


def get_all_album_songs_by_album_id(album_id: str, username: str):
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.users.data import UsersData
    from Core.helpers import flatten_nested_list, remove_duplicates_from_list
    import Monitoring.configurator as config
    import Monitoring.logger as logger
    # CR: format {album_id}
    logger.add_info("getting all songs by album id: %s" % album_id)
    # CR: not pythonic
    album_songs = list()
    # CR: album id is unique. If you would have ordered the data in a way you can access the albums by themselves you
    #  could have found the album withot all this logic
    for artist in SpotipyData().artists:
        # CR: very complicated. Either comment to explain or simplify
        if [track.name for album in artist.albums for track in album.tracks if album.id == album_id]:
            album_songs.append(
                [track.name for album in artist.albums for track in album.tracks if album.id == album_id])
    # CR: same for limiter as above
    return remove_duplicates_from_list(flatten_nested_list(album_songs))[
                   :int(config.config_data['SEARCH_DATA'][
                            'FREE_USER_MAX_RESULTS'])] if UsersData().get_user_permission_level(
                username) == 'free' else remove_duplicates_from_list(flatten_nested_list(album_songs))


# CR: never used username
def get_all_artist_tracks_by_artist_id(artist_id: str, username: str):
    from Core.music_structures.spotipy_data import SpotipyData
    songs = []
    for artist in SpotipyData().artists:
        if artist.id == artist_id:
            songs = [track for album in artist.albums for track in album.tracks]
    return songs


# CR: never used username
def get_most_popular_artist_tracks_by_artist_id(artist_id: str, username: str):
    import Monitoring.configurator as config
    # CR: username?
    songs = get_all_artist_tracks_by_artist_id(artist_id)
    songs.sort(key=lambda track: track.popularity)
    # CR: same for limiter as above
    return songs[:int(config.config_data['SEARCH_DATA']['POPULAR_SONGS'])]
