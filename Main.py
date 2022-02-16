def main():
    # CR: why are you importing inside the main?
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    # CR: unused
    from Core.IO.File import json_file_writer
    import Monitoring.configurator as config
    # CR: unused
    from Core.music_structures.search import get_most_popular_artist_tracks_by_artist_id, get_all_artists
    data = SpotipyData()
    data.load_data(read_all_json_files_from_directory(config.config_data['SONGS_DATA']['DATA_DIR']))
    print(len(get_all_artists('shauli')))


if __name__ == "__main__":
    main()
