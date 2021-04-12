import requests
from bs4 import BeautifulSoup
import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
from sys import exit


with open("default-cred.json","r") as f:
    content = f.read()
    cred = json.loads(content)

CLIENT_ID = cred['CLIENT_ID']
CLIENT_SECRET = cred['CLIENT_SECRET']
USER = cred['USER_ID']

while True:
    try:
        date = input("Input date in format yyyy-mm-dd (type 'q' to quit): ")
        
        if date == "q":
            exit()
        else:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        break
    except Exception as e: 
        print(e)
        print('Invalid date! Please input date in format yyyy-mm-dd')
# date = "2013-12-31"

billboard_url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(f"{billboard_url}{date}")
soup = BeautifulSoup(response.text,"html.parser")
title_tags = soup.find_all('span',class_="chart-element__information__song text--truncate color--primary")
titles = [title.getText() for title in title_tags]
artist_tags = soup.find_all('span',class_="chart-element__information__artist text--truncate color--secondary")
artists = [artist.getText() for artist in artist_tags]
songs=[]
for title in titles:
    song = {'title':title,'artist':artists[titles.index(title)]}
    songs.append(song)

auth_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify( 
        auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://blog.tdinvoke.net/",
        client_id=CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    ))

playlists = sp.user_playlists(USER)


new_playlist_name = f"hot-100-{date}"

# search songs
song_uris = []
year = date.split("-")[0]
for song in songs:
    q = f"track:{song['title']} year:{year}"
    result = sp.search(q=q,type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song['title']} doesn't exist in Spotify. Skipped.")

if not any(playlist['name']==new_playlist_name for playlist in playlists['items']):
    new_playlist = sp.user_playlist_create(user=USER,name=new_playlist_name,public=False)
    print(new_playlist)

sp.playlist_add_items(new_playlist['id'],song_uris)