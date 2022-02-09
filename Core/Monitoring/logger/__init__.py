import logging

#this is the variable which we will use to log everything that we need
logger = logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')