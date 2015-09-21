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
from tokenUtils import *
from userUtils import *
import time
from dbUtils import dbSelectLast

if __name__ == '__main__':
    start = dbSelectLast()[u'user_id']
    print "Starting at {}".format(start)

    args = docopt(__doc__)

    if args['-s']:
        start = int(args['ID'])

    #Get valid tokens from the token file
    valid_tokens = get_tokens()
    get_users(valid_tokens, start)
