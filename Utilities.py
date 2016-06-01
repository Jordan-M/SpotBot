# File: Utilities.py
# Description: A set of methods used for issuing official twitch  moderation commands.
#              A list of all commands can be found here:
#              http://help.twitch.tv/customer/portal/articles/659095-chat-moderation-commands

import Config


#  Function: chat
#  Description: Send a chat message to the server
def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(Config.CHAN, msg))


# Function: ban
# Description: Ban a user from the chat
def ban(sock, user):
    chat(sock, ".ban {}".format(user))


# Function: timeout
# Description: Time out a user for a set period of time
def timeout(sock, user, seconds=600):
    chat(sock, ".timeout {}".format(user, seconds))

