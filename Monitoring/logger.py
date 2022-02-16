import logging
import Monitoring.configurator as config

# CR: if you already use config so put the format in config
# this is the variable which we will use to log everything that we need
logging.basicConfig(filename=config.config_data['LOGGER']['PATH'], filemode='a',
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


# CR: are these methods this really needed?
def add_info(string):
    logging.info(string)


def add_warning(string):
    logging.warning(string)


def add_error(string):
    logging.error(string)
