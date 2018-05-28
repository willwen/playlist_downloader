from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


# because spotily limits 100 results every time, so you have to call this multipel times
def get_playlist_tracks(username, playlist_id):
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    for track in tracks:
        print("{}:{}".format(track["track"]["name"], track["track"]["artists"][0]["name"]))
    while results['next']:
        results = sp.next(results)
        tracks = results['items']
        for track in tracks:
            print("{}:{}".format(track["track"]["name"], track["track"]["artists"][0]["name"]))


# You can either provide a client_id and client_secret to the constructor
# or set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables

# get creds here : https://beta.developer.spotify.com/dashboard/login
client_credentials_manager = SpotifyClientCredentials(
    client_id="",
    client_secret=""
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:1193804728:playlist:3r9ZPi7YLZPwo2WSbdCifT'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

get_playlist_tracks(username, playlist_id)
