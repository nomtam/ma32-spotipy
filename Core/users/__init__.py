from Core.IO.File import read_data_from_json_file
from Core.IO.File import json_file_writer
from Monitoring.exceptions import UsernameIsNotExistError
import Monitoring.logger as logger
import Monitoring.configurator as config

PASSWORD = 0


class UsersData:
    def __init__(self):
        self.data = {}

    def get_users_data(self, file_path=config.config_data['USERS_DATA']['USERS_PATH'],
                       function=read_data_from_json_file):
        self.data = function(file_path)

    def login(self, user: str, password: str):
        if user in self.data.keys():
            return self.data[user][PASSWORD] == password
        else:
            logger.add_error(UsernameIsNotExistError(user))
            return False

    def signup(self, user: str, password: str, user_permission: str):
        if user not in self.data.keys():
            if user_permission.lower() in config.config_data['USERS_DATA']['PERMISSION_LEVELS']:
                self.data[user] = [password, user_permission]
                return True
            else:
                return "user permission is incorrect. can be one of the three" + config.config_data['USERS_DATA'][
                    'PERMISSION_LEVELS']
        else:
            logger.add_info("username already in use")
            return "username already in use"

    def save_data(self, file_path=config.config_data['USERS_DATA']['USERS_PATH']):
        try:
            json_file_writer(file_path, self.data)
        except Exception:
            logger.add_error("problem writing to file")
