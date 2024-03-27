from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from api_keys_secret import *

# Ask user for time travel date
# date = input("Set the dial to what date (YYYY-MM-DD)? ")

# Testing code only
date = '2020-01-01'
year = date.split('-')[0]

# Get list of song titles
billboard_url = "https://www.billboard.com/charts/hot-100/" + date + "/"
billboard_raw = requests.get(billboard_url).text
billboard_soup = BeautifulSoup(markup=billboard_raw, features='html.parser')
hot100_list_raw = billboard_soup.select(selector='ul li h3')
hot100_list_text = [song.getText().strip() for song in hot100_list_raw]
hot100_list_text = hot100_list_text[:100]

# Authenticate on Spotify using Spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri=SPOTIFY_REDIRECT,
        username=SPOTIFY_USERNAME,
        show_dialog=True,
        cache_path=".cache-nhofmeister_secret",
        scope='playlist-modify-private',
    )
)
user_id = sp.current_user()["id"]

# Create list of Spotify song URIs (e.g., 'spotify:track:6rqhFgbbKwnb9MLmUQDhG6')
uri_list = []
for song_title in hot100_list_text:
    search_result = sp.search(q=f"track: {song_title} year: {year}", limit=1, type='track')
    try:
        result_uri = search_result['tracks']['items'][0]['uri']
        uri_list.append(result_uri)
    except IndexError:
        print(f"{song_title} doesn't exist in Spotify. Skipped.")

# Create new Spotify playlist
playlist_name = f"{date} Billboard 100"
new_playlist_response = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    collaborative=False,
    description="100daypy - automatically created playlist"
)
new_playlist_id = new_playlist_response['id']
sp.playlist_add_items(playlist_id=new_playlist_id, items=uri_list, position=None)

pass
