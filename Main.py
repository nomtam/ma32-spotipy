def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.IO.File import read_data_from_json_file
    import Monitoring.configurator as config
    print(read_data_from_json_file(config.config_data['USERS_DATA']['USERS_PATH']))


if __name__ == "__main__":
    main()
