from Core.music_structures.basic_structures.Track import Track


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.tracks = list()  # the list of all tracks of this Album

    def add_song_to_album(self, track: Track):
        self.tracks.append(track)

    def is_track_exist(self, track_id: str):
        for track in self.tracks:
            if track.id == track_id:
                return True
        return False
