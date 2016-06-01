# File: OpOperations.py
# Description: A set of methods that keeps track of the operators/mods in chat

import Config
import urllib2
import json
from time import sleep


# Function: thread_fill_op_list
# Description: In a separate thread, fill up the op list
def thread_fill_op_list():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/CHANNLETOJOIN/chatters"
            req = urllib2.Request(url, headers={"accept": "*/*"})
            response = urllib2.urlopen(req).read()
            if response.find("502 Bad Gateway") == -1:
                Config.opList.clear()
                data = json.loads(response)
                for p in data["chatters"]["moderators"]:
                    Config.opList[p] = "mod"
                for p in data["chatters"]["global_mods"]:
                    Config.opList[p] = "global_mod"
                for p in data["chatters"]["admins"]:
                    Config.opList[p] = "admin"
                for p in data["chatters"]["staff"]:
                    Config.opList[p] = "staff"
        except:
           'do nothing'
        sleep(5)


# Function: is_op
# Description: Returns true if the passed user parameter is in the op list
# Returns: The mod status of user (bool)
def is_op(user):
    return user in Config.opList
