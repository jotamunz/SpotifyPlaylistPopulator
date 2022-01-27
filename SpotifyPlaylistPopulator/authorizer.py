import json
import requests


def refresh_auth(refresh_token, credentials):
    """
    :param refresh_token: (str) Refresh token from OAuth
    :param credentials: (str) Base 64 client_id:client_secret
    :return access_token: (str) new authorization token
    """
    url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        url,
        data={
            "grant_type": "refresh_token",
            "refresh_token": f"{refresh_token}"
        },
        headers={
            "Authorization": f"Basic {credentials}"
        }
    )
    response_json = response.json()
    return response_json["access_token"]
