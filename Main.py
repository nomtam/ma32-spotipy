
def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.IO.File import json_file_writer
    import Monitoring.configurator as config
    from Core.music_structures.search import get_all_album_songs_by_album_id
    data = SpotipyData()
    data.load_data(read_all_json_files_from_directory(config.config_data['SONGS_DATA']['DATA_DIR']))
    print(get_all_album_songs_by_album_id('62U7xIHcID94o20Of5ea4D'))




if __name__ == "__main__":
    main()
