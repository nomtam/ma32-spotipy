from Core.music_structures.basic_structures.Track import Track
from Core.users.data import UsersData
from Core.IO.File import read_data_from_json_file, if_file_exists, create_new_file, json_file_writer
import Monitoring.configurator as config
import Monitoring.logger as logger
from Monitoring.exceptions import FileDoesNotExistError

LOWEST_PERMISSION = "free"


def add_new_playlist(playlist_name: str, username: str):
    user_permission = UsersData().get_user_permission_level(username)
    user_data = get_user_playlist(username)
    if user_permitted_to_add_playlist(user_permission, user_data):
        user_data[playlist_name] = []
        return "playlist added!"
    else:
        return "you are not allowed to add playlist!"


def add_track_to_playlist(username: str, playlist_name: str, track: Track):
    user_permission = UsersData().get_user_permission_level(username)
    user_data = get_user_playlist(username)
    if user_permitted_to_add_song_to_playlist(user_permission, user_data, playlist_name):
        user_data[playlist_name].append(track)
        return "song added successfully!"
    else:
        return "you are not allowed to add song to playlist!"


def get_user_playlist(username):
    file_path = config.config_data["USERS_DATA"]['PLAYLIST_DIR'] + "\\" + username + ".json"
    logger.add_info("reciving playlist data from file: %s" % file_path)

    if if_file_exists(file_path):
        user_data = read_data_from_json_file(file_path)
    else:
        logger.add_error(FileDoesNotExistError(file_path))
        user_data = {}
        create_new_file(file_path)
        logger.add_info("created new playlist file for user: %s" % username)
    return user_data


def user_permitted_to_add_playlist(user_permission: str, user_data: dict):
    return not ((user_permission is LOWEST_PERMISSION) and (len(user_data) == config.config_data['USERS_DATA'][
        'MAX_FREE_PLAYLISTS']))


def user_permitted_to_add_song_to_playlist(user_permission: str, user_data: dict, playlist_name: str):
    return not ((user_permission is LOWEST_PERMISSION) and (
                len(user_data[playlist_name]) == config.config_data['USERS_DATA']['MAX_FREE_SONGS']))
