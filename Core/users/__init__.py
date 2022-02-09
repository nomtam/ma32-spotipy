from Core.IO.File import read_data_from_json_file
from Monitoring.exceptions import UsernameIsNotExistError
import Monitoring.logger as logger
import Monitoring.configurator as config


def get_users_data(file_path, function=read_data_from_json_file):
    return function(file_path)


def login(user: str, password: str, data: dict):
    if user in data.keys():
        return data[user] == password
    else:
        logger.add_error(UsernameIsNotExistError(user))
        return False


def signup(user: str, password: str, data: dict, user_permission: str):
    if user not in data.keys():
        if user_permission.lower() in config.config_data['USERS_DATA']['PERMISSION_LEVELS']:
            data[user] = [password, user_permission]
        else:
            return "user permission is incorrect. can be one of the three" + config.config_data['USERS_DATA'][
                'PERMISSION_LEVELS']
    else:
        return "username already in use"
