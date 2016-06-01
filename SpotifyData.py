# SpotifyData.py
# Description:  Stores all of the data for a spotify session. I feel like this
#               solution is extremely sloppy and can be improved on. I will look into
#               a better way of doing things here.

import WebHandler


class SpotifyData:

    spotify_data = WebHandler.get_spotify_info()
    last_spotify_data = spotify_data
    is_song_new = True

    # Function: __init__
    # Description:  Parses the JSON data returned from WebHandler.py
    #               and initializes the data in this class.
    def __init__(self):
        self.private_session = SpotifyData.spotify_data["open_graph_state"]["private_session"]

        self.artist_name = SpotifyData.spotify_data["track"]["artist_resource"]["name"]

        self.album_name = SpotifyData.spotify_data["track"]["album_resource"]["name"]

        self.track_name = SpotifyData.spotify_data["track"]["track_resource"]["name"]

        self.artist_url = SpotifyData.spotify_data["track"]["artist_resource"]["location"]["og"]

        self.album_url = SpotifyData.spotify_data["track"]["album_resource"]["location"]["og"]

        self.track_url = SpotifyData.spotify_data["track"]["track_resource"]["location"]["og"]

        self.last_artist_name = SpotifyData.last_spotify_data["track"]["artist_resource"]["name"]

        self.last_album_name = SpotifyData.last_spotify_data["track"]["album_resource"]["name"]

        self.last_track_name = SpotifyData.last_spotify_data["track"]["track_resource"]["name"]

        self.last_artist_url = SpotifyData.last_spotify_data["track"]["artist_resource"]["location"]["og"]

        self.last_album_url = SpotifyData.last_spotify_data["track"]["album_resource"]["location"]["og"]

        self.last_track_url = SpotifyData.last_spotify_data["track"]["track_resource"]["location"]["og"]

    # Function: refresh
    # Description:  Grabs the newest version of Spotify information from
    #               WebHandler.py and updates the info in this class if
    #               it is newer.
    def refresh(self):
        new_data = WebHandler.get_spotify_info()
        new_track_url = new_data["track"]["track_resource"]["location"]["og"]
        current_track_url = SpotifyData.spotify_data["track"]["track_resource"]["location"]["og"]

        # If the new JSON data is different from the current data,
        # update last_spotify_data and replace spotify_data with the data we just pulled.
        # Track URL is what determines if the data is the same.
        if new_track_url != current_track_url:
            SpotifyData.last_spotify_data = SpotifyData.spotify_data
            SpotifyData.spotify_data = new_data
        # Reinitialize all data. This may be bad practice? I will change if necessary.
            SpotifyData.__init__(self)
            SpotifyData.is_song_new = True
        else:
            SpotifyData.is_song_new = False
