import Utilities
import time
from SpotifyData import SpotifyData


spotify_data = SpotifyData()


def handle_command(user, message, socket):
    if message == "!time":
        Utilities.chat(socket, "The time is: " + time.strftime("%I:%M %p %Z on %A, %B %d, %Y."))

    elif message == "!message":
        Utilities.chat(socket, "This is a test message")

    elif message == "!admin":
        Utilities.chat(socket, "You are admin: %s" % Utilities.isOp(user))

    elif message == "!song":
        spotify_data.refresh()
        Utilities.chat(socket, spotify_data.track_name + " - " + spotify_data.track_url)

    elif message == "!artist":
        spotify_data.refresh()
        Utilities.chat(socket, spotify_data.artist_name + " - " + spotify_data.artist_url)

    elif message == "!album":
        spotify_data.refresh()
        Utilities.chat(socket, spotify_data.album_name + " - " + spotify_data.album_url)
