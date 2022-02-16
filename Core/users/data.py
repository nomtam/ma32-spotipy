from Core.IO.File import read_data_from_json_file
from Core.IO.File import json_file_writer
from Monitoring.exceptions import UsernameIsNotExistError
import Monitoring.logger as logger
import Monitoring.configurator as config
# CR: using [PASSSWORD] is better than [0]. But the best practice is to load the data into a class and than access it
PASSWORD = 0
PERMISSION_LEVEL = 1


# this class will be in singleton state in order to save memory and working with it in different places in need
# CR: if you are using ['USER_DATA'] everywhere. Why not save it in a var instead of accessing it multiple times?
class UsersData:
    __instance = None

    # this class is to create the singleton state
    class __UsersSingletonHelper:
        # CR: get_id
        def getid(self):
            return id(self)

        # CR: config the strings
        # CR: function is bad naming. Why not "reader"?
        def __init__(self, file_path=config.config_data['USERS_DATA']['USERS_PATH'],
                     function=read_data_from_json_file):
            self.data = function(file_path)

        def login(self, user: str, password: str):
            if user in self.data.keys():
                # CR: see comment above
                return self.data[user][PASSWORD] is password
            else:
                logger.add_error(UsernameIsNotExistError(user))
                return False

        def signup(self, user: str, password: str, user_permission: str):
            if user not in self.data.keys():
                if user_permission.lower() in config.config_data['USERS_DATA']['PERMISSION_LEVELS']:
                    self.data[user] = [password, user_permission]
                    # CR: never closes
                    # CR: why not with open?
                    # CR: coupled to json
                    # CR: SRP
                    # CR: OCP
                    open(config.config_data["USERS_DATA"]['PLAYLIST_DIR'] + "\\" + user + ".json", "w")
                    return True
                else:
                    # CR: again returning a String is not good
                    return "user permission level is incorrect. can be one of the three" + \
                           config.config_data['USERS_DATA'][
                               'PERMISSION_LEVELS']
            else:
                logger.add_info("username already in use")
                return "username already in use"

        def save_data(self, file_path=config.config_data['USERS_DATA']['USERS_PATH']):
            try:
                # CR: coupled to json. Why not use DIP?
                json_file_writer(file_path, self.data)
            # CR: too broad exception
            except Exception:
                # CR: why not IOError and check it
                logger.add_error("problem writing to file")

        def get_user_permission_level(self, username: str):
            # CR: check comment above
            return self.data[username][PERMISSION_LEVEL]

    # CR: function is bad naming. "reader"?
    def __init__(self, file_path=config.config_data['USERS_DATA']['USERS_PATH'], function=read_data_from_json_file):
        if UsersData.__instance is None:
            UsersData.__instance = UsersData.__UsersSingletonHelper(file_path, function)
        self.__dict__['singleton_instance'] = UsersData.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
