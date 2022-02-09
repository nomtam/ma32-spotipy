import logging
import Monitoring.configurator as config

# this is the variable which we will use to log everything that we need
logging.basicConfig(filename=config.config_data['LOGGER']['PATH'], filemode='a',
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')


def add_info(string):
    logging.info(string)


def add_warning(string):
    logging.warning(string)


def add_error(string):
    logging.error(string)
