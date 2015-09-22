#!/usr/bin/python
"""
    Instagram Scraper - It does cool shit.

    Usage:
        main.py [-s ID]

    Options:
        -h --help   Show this screen.
        -s  Start at a specific user id
"""
from docopt import docopt
from lib.tokenUtils import *
from lib.userUtils import *
import time

if __name__ == '__main__':

    start = 1

    args = docopt(__doc__)

    if args['-s']:
        start = args['ID']

    #Get valid tokens from the token file
    valid_tokens = get_tokens()
    get_users(valid_tokens, start)
