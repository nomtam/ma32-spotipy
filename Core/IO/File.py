import os, json
import Monitoring.logger as logger
from Monitoring.exceptions import PathIsNotFileError
from Monitoring.exceptions import FileIsNotCorrectError


def read_data_from_json_file(file_path):
    if os.path.isfile(file_path):
        if file_path.endswith(".json"):
            return json.load(open(file_path, 'r'))
        else:
            logger.add_error(FileIsNotCorrectError("json", file_path))
    else:
        logger.add_error(PathIsNotFileError(file_path))
