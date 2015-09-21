import requests, random, progressbar, time, ConfigParser, sys, traceback
from tokenUtils import *
from dbUtils import dbInsert
from multiprocessing import Process, Lock, Queue, current_process
from loggingUtils import getLogger

logger = getLogger(__name__)
all_tokens = None

def config():
    c = ConfigParser.ConfigParser()
    opts = c.read(open('./config.ini'))
    print opts
    quit()

def getUser(id, token):
    global logger
    payload = {'access_token': token['token']}
    url = "https://api.instagram.com/v1/users/{}".format(str(id))

    r = requests.get(url, params=payload)

    if r.status_code != 200:
        logger.warning("Error getting user {}: {}".format(id, r.text))
        return False
    else:
        logger.info("Successfully got user {}: {}".format(id, r.text))
	
	if r.json()['data']['counts']['followed_by'] >= 5000: 
		try:
            		dbInsert(format_user(r.json()))
        	except:
            		exception = sys.exc_info()
            		print exception
            		print traceback.format_exc()
            		quit()
        
	return r.json()

def user_worker(work_queue, done_queue):
    """
        Checks for users in a multiprocessing thingy
    """
    for data in iter(work_queue.get, 'STOP'):
        user = getUser(data['id'], data['token'])

        if user and 'data' in user:
            done_queue.put(format_user(user))

    return True

def get_users(tokens, start=1):
    """
        Runs processes to find all users
    """

    user_ids = xrange(start, start+100)
    workers = 200
    work_queue = Queue()
    done_queue = Queue()
    processes = []

    try:
        for user_id in user_ids:
            updated_tokens = getRandomToken(tokens)
            token = updated_tokens['chosen_token']
            tokens = updated_tokens['all_tokens']

            work_queue.put({'id': user_id, 'token': token})
    except:
        exception = sys.exc_info()
        print exception
        quit()

    for w in xrange(workers):
        p = Process(target=user_worker, args=(work_queue, done_queue))
        p.start()
        processes.append(p)
        work_queue.put('STOP')

    for p in processes:
        p.join()

    done_queue.put('STOP')

    if user_ids[-1] <= 10**9:
        get_users(tokens, user_ids[-1])

    return True

def format_user(user):
    vals = [user['data']['username'],
            user['data']['full_name'],
            user['data']['bio'],
            user['data']['website'],
            user['data']['profile_picture'],
            user['data']['counts']['media'],
            user['data']['counts']['followed_by'],
            user['data']['counts']['follows'],
            user['data']['id']]

    for val in vals:
        if isinstance(val, unicode):
            val = val.encode('utf-8')

    return vals
