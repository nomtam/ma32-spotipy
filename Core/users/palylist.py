from Core.users.data import UsersData
from Core.IO.File import read_data_from_json_file
import Monitoring.configurator as config


def add_new_playlist(playlist_name: str, username: str):
    user_permission = UsersData().get_user_permission_level(username)
    user_data = read_data_from_json_file(config.config_data["USERS_DATA"]['PLAYLIST_DIR'] + "\\" + username + ".json")

# def add_song_to_playlist(playlist_name: str, username: str):
