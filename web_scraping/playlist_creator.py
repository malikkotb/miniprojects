from pprint import pprint
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{str(date)}/"

response = requests.get(URL)
charts = response.text

soup = BeautifulSoup(charts, "html.parser")
songs = soup.select(selector="li h3")

song_titles = [song.getText().strip("\n\n\t\n\t\n\t\t\n\t\t\t\t\t") for song in songs]
song_titles = [song_titles[i] for i in range(100)]

print(song_titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))

user_id = sp.current_user()["id"]

# use spotipy docs to create list of song URIs for the list of song names
song_uris = []
query = f"track: {'Dynamite'} year: {2020}"
uri = sp.search(query, type='track', market=None)
for song in song_titles:
     query = f"track: {song} year: {date[0:4]}"
     try:
        uri = sp.search(query, type='track', market=None)['tracks']['items'][0]['uri']
        song_uris.append(uri)
     except IndexError:
         print(f"{song} doesn't exist in Spotify. Skipped")
pprint(song_uris)


playlist = sp.user_playlist_create(user_id, f"Throwback to {date}", public=False, collaborative=False,
                                   description=f"Throwback to {date} and the top 100 songs of that week.")
print(playlist)
sp.playlist_add_items(playlist["id"], items=song_uris, position=None)
