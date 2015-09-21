import logging

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)

    handler = logging.FileHandler('log.log')
    handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
