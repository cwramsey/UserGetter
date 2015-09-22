from slacker import Slacker
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

def alert(msg, room='#general'):
    slack = Slacker(config.get('slack', 'token'))
    slack.chat.post_message(room, msg)
