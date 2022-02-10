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

        def load_data(self, data: list):
            logger.add_info("loading data into basic structures")
            for track in data:
                for artist in track['track']['artists']:
                    try:
                        if self.if_artist_exist(artist['id']) is NOT_FOUND:
                            # new artist means everything is new
                            new_artist = Artist(artist['id'], artist['name'])
                            new_artist.add_album(Album(track['track']['album']['id'], track['track']['album']['name']))
                            new_artist.add_song_to_album(track['track']['album']['id'],
                                                         Track(track['track']['id'], track['track']['name'],
                                                               int(track['track']['popularity'])))
                            self.add_artist(new_artist)
                        else:
                            artist_index = self.if_artist_exist(artist['id'])
                            if not self.artists[artist_index].if_album_exists(track['track']['album']['id']):
                                self.artists[artist_index].add_album(
                                    Album(track['track']['album']['id'], track['track']['album']['name']))
                            self.artists[artist_index].add_song_to_album(track['track']['album']['id'],
                                                                         Track(track['track']['id'],
                                                                               track['track']['name'],
                                                                               int(track['track']['popularity'])))
                    except KeyError:
                        logger.add_error(KeyWordDoesNotExistError(track['track']))
            logger.add_info("finished loading data into basic structure")

        def add_artist(self, artist: Artist):
            self.artists.append(artist)

        def if_artist_exist(self, artist_id: str):
            for index, artist in enumerate(self.artists):
                if artist.id == artist_id:
                    return index
            return NOT_FOUND

        def get_data(self):
            return self.artists

    def __init__(self):
        if SpotipyData.__instance is None:
            SpotipyData.__instance = SpotipyData.__SpotipyDataSingleton()
        self.__dict__['singleton_instance'] = SpotipyData.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
