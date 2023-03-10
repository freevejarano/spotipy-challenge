import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app_id = "your_app_id"
app_secret = "your_app_secret"

# Get credentials from file
with open('credentials.txt') as f:
    credentials = f.read().splitlines()
    app_id = credentials[0]
    app_secret = credentials[1]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=app_id,
                                                           client_secret=app_secret))

# Example of getting a track
results = sp.search(q='After Hours', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])