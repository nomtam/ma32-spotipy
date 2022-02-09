def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    data = read_all_json_files_from_directory()
    spotipy_data = SpotipyData()
    spotipy_data.load_data(data)
    m_data = spotipy_data.get_data()
    for artist in m_data:
        print(artist.name, end='-')
        for album in artist.albums:
            print(album.name, end=":")
            for track in album.tracks:
                print(track.name, end=',')
        print()


if __name__ == "__main__":
    main()
