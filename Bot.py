# File: Bot.py
# Description: The bots main logic and entry point

import Config
import Utilities
import OpOperations
import socket
import re
import thread
import CommandHandler
from time import sleep


def main():
    s = socket.socket()
    s.connect((Config.HOST, Config.PORT))
    s.send("PASS {}\r\n".format(Config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(Config.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(Config.CHAN).encode("utf-8"))

    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    Utilities.chat(s, "SpotBot has started running!")

    thread.start_new_thread(OpOperations.thread_fill_op_list, ())

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            user = re.search(r"\w+", response).group(0)
            message = chat_message.sub("", response)
            message = message.strip()
            CommandHandler.handle_command(user, message, s)
            print(response)
        sleep(1)

if __name__ == "__main__":
    main()