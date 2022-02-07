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
        offset = 100
        while tracks and len(tracks) == offset:
            params = {"offset": offset}
            response = self._place_get_api_request(url, params)
            response_json = response.json()
            tracks += [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                       track in response_json["items"]]
            offset += 100
        return tracks

    def populate_playlist(self, playlist_id, tracks):
        """
        :param playlist_id: (str) Spotify playlist id
        :param tracks: ([Track]) List of tracks to add
        :return
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        batches = len(track_uris) // 100
        for i in range(batches):
            data = json.dumps(track_uris[:100])
            self._place_post_api_request(url, data)
            track_uris = track_uris[100:]
        if track_uris:
            data = json.dumps(track_uris)
            self._place_post_api_request(url, data)
        return

    def clear_playlist(self, playlist_id):
        """
        :param playlist_id: (str) Spotify playlist id
        :return
        """
        tracks = self.get_playlist_tracks(playlist_id)
        track_uris = [track.create_spotify_uri_json() for track in tracks]
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        batches = len(track_uris) // 100
        for i in range(batches):
            data = json.dumps({"tracks": track_uris[:100]})
            self._place_del_api_request(url, data)
            track_uris = track_uris[100:]
        if track_uris:
            data = json.dumps({"tracks": track_uris})
            self._place_del_api_request(url, data)
        return

    def _place_get_api_request(self, url, params=None):
        response = requests.get(
            url,
            params=params,
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
