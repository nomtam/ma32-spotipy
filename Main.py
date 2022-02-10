def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.IO.File import json_file_writer
    import Monitoring.configurator as config
    from Core.music_structures.search import get_most_popular_artist_tracks_by_artist_id
    data = SpotipyData()
    data.load_data(read_all_json_files_from_directory(config.config_data['SONGS_DATA']['DATA_DIR']))
    print(get_most_popular_artist_tracks_by_artist_id('7oPftvlwr6VrsViSDV7fJY'))


if __name__ == "__main__":
    main()
