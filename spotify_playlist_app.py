from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input('When do you want to travel to? (yyyy-mm-dd) ')

# Scrape Billboard 100
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
billboard_html = response.text
soup = BeautifulSoup(billboard_html, 'html.parser')
song_tags = soup.find_all(name='h3', class_='a-no-trucate', limit=100)
song_text = [tag.getText() for tag in song_tags]
song_list = [re.sub(r"[\n\t]*", '', song) for song in song_text]
artist_tags = soup.find_all(name='span', class_='a-no-trucate', limit=100)
artist_text = [tag.getText() for tag in artist_tags]
artist_list = [re.sub(r"[\n\t]*", '', artist) for artist in artist_text]

# Spotipy authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Getting song URIs
song_uri = []
queries = list(zip(song_list, artist_list))
for track in queries:
    results = sp.search(q=f'track:{track[0]} artist:{track[1]}', type='track')
    try:
        uri = results['tracks']['items'][0]['uri']
    except IndexError:
        pass
    else:
        song_uri.append(uri)

# Creating and adding songs to playlist
playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
