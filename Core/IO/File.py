import os
import json
import Monitoring.logger as logger
from Monitoring.exceptions import PathIsNotFileError
from Monitoring.exceptions import FileIsNotCorrectError


# CR: read_json
def read_data_from_json_file(file_path: str):
    if os.path.isfile(file_path):
        if file_path.endswith(".json"):
            try:
                # CR: no close?
                # CR: use with open
                return json.load(open(file_path, 'r'))
            except IOError:
                logger.add_error(IOError("problem reading file"))
        else:
            # CR: file type is a better error name
            logger.add_error(FileIsNotCorrectError("json", file_path))
    else:
        logger.add_error(PathIsNotFileError(file_path))


# CR: write_json
def json_file_writer(file_path: str, data: dict):
    if os.path.isfile(file_path):
        if file_path.endswith(".json"):
            try:
                # CR: same about close
                # CR: same about with open
                file = open(file_path, 'w')
                json.dump(data, file)
            except IOError:
                logger.add_error(IOError("problem writing to file"))
        else:
            # CR: same about error
            logger.add_error(FileIsNotCorrectError("json", file_path))
    else:
        logger.add_error(PathIsNotFileError(file_path))


# CR: does_file_exist
# CR: why to make a method to replace one line?
def if_file_exists(file_path: str):
    return os.path.exists(file_path)


# CR: not the way to create file. Should be:
"""
    with open(file_path, 'w') as f:
        pass
"""


def create_new_file(file_path):
    open(file_path, 'w')
