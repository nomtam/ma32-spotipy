
def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    from Core.music_structures.spotipy_data import SpotipyData
    from Core.IO.File import json_file_writer
    import Monitoring.configurator as config
    from Core.users.data import UsersData
    data = UsersData()
    print(data.signup("rdg", "123", "free"))
    data.save_data()


if __name__ == "__main__":
    main()
