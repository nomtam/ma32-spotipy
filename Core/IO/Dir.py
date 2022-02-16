import os, json
from pathlib import Path
import Monitoring.logger as logger


# this function as it says, reads all json files from directory, the name is in the config file so o need to insert this
# CR: read_data_from_dir
# CR: json should be by DIP
# CR: path_to_dir is a better name
# CR: in general I would have thought this method would do a loop on all the files you found in the dir using
#  the reader from File module. repeating the logic here is weird
def read_all_json_files_from_directory(path_to_json: str):
    logger.add_info("reading all data from directory")
    from Monitoring.exceptions import PathIsNotDirectoryError
    if Path(path_to_json).is_dir():
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        data = []
        for file in json_files:
            # CR: open and no close
            # CR: why not use read json fom file?
            data.append(json.load(open(path_to_json + '\\' + file)))
        return data
    else:
        logger.add_error(PathIsNotDirectoryError(path_to_json))
    # CR: you do this even if you didn't read anything...
    logger.add_info("finished reading all data from directory")
