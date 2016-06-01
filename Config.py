# File: Config.py
# Description: Contains the configuration settings for the bot

import ConfigParser


# Function: config_section_map
# Description:  Parses the config settings for the section passed in and
#               assigns the data to a dictionary
# Returns: Config settings (Dictionary)
def config_section_map(section):
    settings = {}
    options = config.options(section)
    for option in options:
        try:
            settings[option] = config.get(section, option)
        except:
            print("Exception occurred on option: %s." % option)
    return settings


config = ConfigParser.ConfigParser()
config.read("settings.ini")

HOST = config_section_map("Settings")['host']
PORT = int(config_section_map("Settings")['port'])
NICK = config_section_map("Settings")['nick']
PASS = config_section_map("Settings")['pass']
CHAN = config_section_map("Settings")['chan']

# Contains list of mods currently in chat
opList = {}