import os, json
from pathlib import Path
import Monitoring.logger as logger


# this function as it says, reads all json files from directory, the name is in the config file so o need to insert this
def read_all_json_files_from_directory(path_to_json: str):
    logger.add_info("reading all data from directory")
    from Monitoring.exceptions import PathIsNotDirectoryError
    if Path(path_to_json).is_dir():
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        data = []
        for file in json_files:
            data.append(json.load(open(path_to_json + '\\' + file)))
        return data
    else:
        logger.add_error(PathIsNotDirectoryError(path_to_json))
    logger.add_info("finished reading all data from directory")
