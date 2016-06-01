# WebHandler.py
# Description: Handles all internet interactions. Mostly focused on getting information from
#              Spotify's WebHelper.

import urllib2
import json


USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20050519"

# To obtain the CSRF token we must have our origin header set to https://open.spotify.com
ORIGIN_HEADER = "https://open.spotify.com"
HEADERS = {"user-agent": USER_AGENT, "Origin": ORIGIN_HEADER}

# This is the port that Spotify's WebHelper runs on.
PORT = "4380"


# Function: get_spotify_info
# Description: Retrieves info of the current spotify session in JSON format
# Returns: Spotify information in JSON Format (dictionary)
def get_spotify_info():
    oauth = get_oauth()
    csrf = get_csrf()
    url = build_url("/remote/status.json" + "?oauth=" + oauth + "&csrf=" + csrf)
    json_data = get_page(url)
    return json_data


# Function: get_oauth
# Description: Retrieves the OAUTH token for the Spotify user currently logged in 
# Returns: OAuth token (String)
def get_oauth():
    url = "https://open.spotify.com/token"
    json_data = get_page(url)
    return json_data["t"]


# Function: get_csrf
# Description: Retrieves the CSRF token for the Spotify user currently logged in
# Returns: CSRF token (String) 
def get_csrf():
    url = build_url("/simplecsrf/token.json")
    json_data = get_page(url)
    return json_data["token"]


# Function: get_page
# Description: Retrieves the requested url
# Returns: Whatever JSON data was on the requested url page (Dictionary)
def get_page(url):
    request = urllib2.Request(url, headers=HEADERS)
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    return data

# Function: build_url
# Description: Creates a url based on the variable _PORT and the passsed path
# Returns: Url (String)
def build_url(path):
    return "http://127.0.0.1:" + PORT + path


