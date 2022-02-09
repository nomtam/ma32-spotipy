from Core.music_structures.Track import Track


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.tracks = list()  # the list of all tracks of this Album

    def add_song_to_album(self, track : Track):
        self.tracks.append(track)