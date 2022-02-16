from Core.music_structures.basic_structures.Album import Album
from Core.music_structures.basic_structures.Track import Track


class Artist:
    # CR: id shadows
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        # CR: why not a dict { id: data } for better search?
        self.albums = list()  # the list of all tracks of this Album

    def add_album(self, album: Album):
        self.albums.append(album)

    # CR: does instead of if
    # CR: if would have used a dict it wouldnt have to be a method
    def if_album_exists(self, album_id: str):
        for album in self.albums:
            if album.id == album_id:
                return True
        return False

    # CR: same about dict
    def add_song_to_album(self, album_id: str, track: Track):
        for album in self.albums:
            if album.id == album_id:
                album.add_song_to_album(track)
