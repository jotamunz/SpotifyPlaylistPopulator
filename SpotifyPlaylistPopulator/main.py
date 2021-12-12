import os
import random

from spotifyclient import SpotifyClient

from dotenv import load_dotenv
load_dotenv()

SIZE_LIMIT = 100

def populate_target_from_roster():
    spotify_client = SpotifyClient(os.getenv("AUTH_TOKEN"), os.getenv("USER_ID"))

    response = spotify_client.clear_playlist(os.getenv("PLAYLIST_TARGET_1"))
    print(response)

    tracks = spotify_client.get_playlist_tracks(os.getenv("PLAYLIST_ROSTER_1"))

    random.shuffle(tracks)

    size = SIZE_LIMIT
    if len(tracks) < SIZE_LIMIT:
        size = len(tracks)

    response = spotify_client.populate_playlist(os.getenv("PLAYLIST_TARGET_1"), tracks[:size])
    print(response)

if __name__ == '__main__':
    populate_target_from_roster()

