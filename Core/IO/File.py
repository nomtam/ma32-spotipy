import os, json
import Monitoring.logger as logger
from Monitoring.exceptions import PathIsNotFileError
from Monitoring.exceptions import FileIsNotCorrectError


def read_data_from_json_file(file_path: str):
    if os.path.isfile(file_path):
        if file_path.endswith(".json"):
            try:
                return json.load(open(file_path, 'r'))
            except IOError:
                logger.add_error(IOError("problem reading file"))
        else:
            logger.add_error(FileIsNotCorrectError("json", file_path))
    else:
        logger.add_error(PathIsNotFileError(file_path))


def json_file_writer(file_path: str, data: dict):
    if os.path.isfile(file_path):
        if file_path.endswith(".json"):
            try:
                file = open(file_path, 'w')
                json.dump(data, file)
            except IOError:
                logger.add_error(IOError("problem writing to file"))
        else:
            logger.add_error(FileIsNotCorrectError("json", file_path))
    else:
        logger.add_error(PathIsNotFileError(file_path))
