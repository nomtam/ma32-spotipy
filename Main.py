
def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.IO.File import json_file_writer
    import Monitoring.configurator as config
    data = SpotipyData()
    data.load_data(read_all_json_files_from_directory(config.config_data['SONGS_DATA']['DATA_DIR']))





if __name__ == "__main__":
    main()
