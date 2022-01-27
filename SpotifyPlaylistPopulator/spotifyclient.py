import json
import requests

from track import Track


class SpotifyClient:

    def __init__(self, authorization_token, user_id):
        """
        :param authorization_token: (str) Spotify API token
        :param user_id: (str) Spotify user id
        """
        self._authorization_token = authorization_token
        self._user_id = user_id

    def get_playlist_tracks(self, playlist_id):
        """
        :param playlist_id: (str) Spotify playlist id
        :return tracks: ([Track]) List of playlist tracks
        """
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                  track in response_json["items"]]
        return tracks

    def populate_playlist(self, playlist_id, tracks):
        """
        :param playlist_id: (str) Spotify playlist id
        :param tracks: ([Track]) List of tracks to add
        :return response: API response
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def clear_playlist(self, playlist_id):
        """
        :param playlist_id: (str) Spotify playlist id
        :return response: API response
        """
        tracks = self.get_playlist_tracks(playlist_id)
        track_uris = [track.create_spotify_uri_json() for track in tracks]
        data = json.dumps({"tracks": track_uris})
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = self._place_del_api_request(url, data)
        response_json = response.json()
        return response_json

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response

    def _place_del_api_request(self, url, data):
        response = requests.delete(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response
