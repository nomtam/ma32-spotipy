from Core.music_structures.basic_structures.Album import Album
from Core.music_structures.basic_structures.Artist import Artist
from Core.music_structures.basic_structures.Track import Track


class SpotipyData:
    def __init__(self):
        self.artists = []

    def load_data(self, data: list):
        for track in data:
            for artist in track['track']['artists']:
                if not self.if_artist_exist(artist['id']):  # new artist means everything is new
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
                                                                 Track(track['track']['id'], track['track']['name'],
                                                                       int(track['track']['popularity'])))

    def add_artist(self, artist: Artist):
        self.artists.append(artist)

    def if_artist_exist(self, artist_id: str):
        for index, artist in enumerate(self.artists):
            if artist.id == artist_id:
                return index
        return False

    def get_data(self):
        return self.artists
