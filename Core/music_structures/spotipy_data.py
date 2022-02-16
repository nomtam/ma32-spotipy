from Core.music_structures.basic_structures.Album import Album
from Core.music_structures.basic_structures.Artist import Artist
from Core.music_structures.basic_structures.Track import Track
import Monitoring.logger as logger
from Monitoring.exceptions import KeyWordDoesNotExistError

NOT_FOUND = -1


class SpotipyData:
    __instance = None

    class __SpotipyDataSingleton:
        def __init__(self):
            self.artists = []

        # CR: super long method. Must be split
        def load_data(self, data: list):
            logger.add_info("loading data into basic structures")
            for track in data:
                # CR: config
                for artist in track['track']['artists']:
                    try:
                        # CR: config - every string should be config
                        # CR: extract to a method
                        # CR: if you access parts multiple time you should make it to a temp var
                        if self.if_artist_exist(artist['id']) is NOT_FOUND:
                            # new artist means everything is new
                            new_artist = Artist(artist['id'], artist['name'])
                            new_artist.add_album(Album(track['track']['album']['id'], track['track']['album']['name']))
                            # CR: put the track c'tor in a var and use it here and in the second place
                            new_artist.add_song_to_album(track['track']['album']['id'],
                                                         Track(track['track']['id'], track['track']['name'],
                                                               int(track['track']['popularity'])))
                            self.add_artist(new_artist)
                        else:
                            # CR: same comments as above
                            artist_index = self.if_artist_exist(artist['id'])
                            if not self.artists[artist_index].if_album_exists(track['track']['album']['id']):
                                self.artists[artist_index].add_album(
                                    Album(track['track']['album']['id'], track['track']['album']['name']))
                                # CR: same comment for track
                            self.artists[artist_index].add_song_to_album(track['track']['album']['id'],
                                                                         Track(track['track']['id'],
                                                                               track['track']['name'],
                                                                               int(track['track']['popularity'])))
                    except KeyError:
                        # CR: what does this mean? What is a key error?
                        logger.add_error(KeyWordDoesNotExistError(track['track']))
            # CR: "Finished loading data" is enough
            logger.add_info("finished loading data into basic structure")

        def add_artist(self, artist: Artist):
            self.artists.append(artist)

        # CR: does_artist_exist
        def if_artist_exist(self, artist_id: str):
            for index, artist in enumerate(self.artists):
                if artist.id == artist_id:
                    # CR: if he exist just return his data...
                    return index
            # CR: true/false
            return NOT_FOUND

        def get_data(self):
            return self.artists

    def __init__(self):
        if SpotipyData.__instance is None:
            SpotipyData.__instance = SpotipyData.__SpotipyDataSingleton()
        self.__dict__['singleton_instance'] = SpotipyData.__instance

    # CR: what is this? why not just save the data in structures? lists, dicts
    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
