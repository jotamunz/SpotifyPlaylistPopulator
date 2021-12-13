import random

from spotifyclient import SpotifyClient
from jsonmanager import read_json


def main():
    config = read_json("settings.json")
    spotify_client = SpotifyClient(config["auth_token"], config["user_id"])
    for playlist in config["playlists"]:
        populate_target_from_roster(spotify_client, playlist["subject_playlist_id"],
                                    playlist["target_playlist_id"], playlist["size_limit"])


def populate_target_from_roster(spotify_client, subject_playlist, target_playlist, size_limit):

    # Get subject playlist tracks
    tracks = spotify_client.get_playlist_tracks(subject_playlist)

    # Shuffle and validate size
    random.shuffle(tracks)
    if len(tracks) < size_limit:
        size_limit = len(tracks)

    # Clear target playlist
    spotify_client.clear_playlist(target_playlist)

    # Populate target playlist
    spotify_client.populate_playlist(target_playlist, tracks[:size_limit])


if __name__ == '__main__':
    main()


