# Spotify Playlist Populator
A Python application to populate a Spotify playlist with tracks from another Spotify playlist using the Spotify Web API

## Install
Install the necessary Python packages by running:

`$ pip install -r requirements.txt`

## Configure
This application uses the OAuth 2.0 authorization framework

Step 1. Register your app in [Spotify for Developers](https://developer.spotify.com/dashboard)

**Note:** save your client_id and client_secret

Step 2. Set a redirect uri (it doesn't have to be a valid uri)

Step 3. Authorize your user by going to the following url

`https://accounts.spotify.com/authorize?client_id=YOUR_ID&response_type=code&redirect_uri=YOUR_URI&scope=playlist-modify-public%20playlist-modify-private%20playlist-read-public%20playlist-read-private%20playlist-read-collaborative`

Directly replace the following params  
YOUR_ID: Your given client id  
YOUR_URI: [URL-encoded](https://www.urlencoder.org) exact match of app redirect uri

**Note:** save the code returned in the url

Step 4. Obtain refresh token by running the following curl command in cmd

`curl -H "Authorization: Basic YOUR_CREDENTIALS" -d grant_type=authorization_code -d code=YOUR_CODE -d redirect_uri=YOUR_URI https://accounts.spotify.com/api/token --ssl-no-revoke`

Directly replace the following params  
YOUR_CREDENTIALS: [Base64-encoded](https://www.base64encode.org) result of `client_id:client_secret`  
YOUR_CODE: Code obtained in previous step  
YOUR_URI: Same as before

**Note:** save the refresh token from the response json

Step 5. Modify the parameters in "SpotifyPlaylistPopulator/settings-example.json"

Use the obtained refresh token and Base64-encoded credentials. The user and playlist ids can be obtained from their corresponding urls or with the [console](https://developer.spotify.com/console).

Step 6. Rename the file to "settings.json"

The application can now be run any time without reauthorizing or any user input. If you need any help refer to [this tutorial](https://www.youtube.com/watch?v=-FsFT6OwE1A)

## Run
Run the entry-point script:

`$ python main.py`




