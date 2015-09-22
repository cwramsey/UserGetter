import logging
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

def log(msg):
    if config.get('env', 'env') == 'dev':
        print msg

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)

    handler = logging.FileHandler('log.log')
    handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
