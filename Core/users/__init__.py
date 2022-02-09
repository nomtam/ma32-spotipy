from Core.IO.File import read_data_from_json_file
from Monitoring.exceptions import UsernameIsNotExistError
import Monitoring.logger as logger

def get_users_data(file_path, function=read_data_from_json_file):
    return function(file_path)


def login(user: str, password: str, data: dict):
    if user in data.keys():
        return data[user] == password
    else:
        logger.add_error(UsernameIsNotExistError(user))
        return False


def signup(user: str, password: str, data: dict, user_permission: str):
    if user in data.keys():
        
    else:
        return False