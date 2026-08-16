#TODO: use the API to look up those track names, get their valid IDs, and automatically build your own playlist

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import sys

hardcoded_ls = [
    ['The Voice in My Heart', 820900], ['Never Coming Back', 616842], ['Theme of Violet Evergarden', 389407], 
    ["A Doll's Beginning", 361189], ['Across the Violet Sky', 348384], ['The Ultimate Price', 310680], 
    ['The Love That Binds Us', 194488], ['Rust', 192945], ['The Long Night', 152603], ['Ink to Paper', 147730], 
    ['One Last Message', 146450], ['To The Ends of Our World', 143345], ['Sincerely (Short Size)', 139415], 
    ["Violet's Letter", 107893], ['In Remembrance', 107325], ['Unspoken Words', 106430], ['Back in Business', 105180], 
    ['Another Sunny Day', 99018], ['Those Words You Spoke to Me', 98020], ['Torment', 98011], 
    ['Violet Snow for Orchestra', 97158], ['What It Means To Love', 95094], ['A Simple Mission', 91447], 
    ['A Place to Call Home', 86243], ['The Birth of a Legend', 73487], ['An Admirable Doll', 68455], 
    ['Adamantine Dreams', 67480], ['Fractured Heart', 66369], ['みちしるべ (Short Size)', 64381], ['Strangeling', 64264], 
    ['Letters From Heaven', 64227], ['Wherever You Are, Wherever You May Be', 63729], ['Inconsolable', 62151], 
    ['Devoid of Hope', 54028], ['Each Memory a Message', 53401], ['Innocence', 52796], ['Always Watching Over You', 50721], 
    ['A Bit of Sass', 50159], ['Letter (Short Size)', 36791], ['The Songstress Aria', 35624], ['Torn Apart at the Seams', 27758], 
    ['Believe In... (Short Size)', 27602], ['The Storm', 26174], ['Intertwined Fates', 25580], 
    ['The Songstress Aria (Instrumental)', 25221], ['The Stench of Fear and Hatred', 23448], ['Violet Snow (Short Size)', 21967]
]
hardcoded_album = "Violet Evergarden: Automemories"


client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_sec = os.environ["SPOTIFY_CLIENT_SECRET"]
redir_uri = "http://127.0.0.1:8000/callback"
scp = "playlist-read-private playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_sec, redirect_uri=redir_uri, scope=scp))
sys.stdout.reconfigure(encoding="utf-8")







for yt_track in hardcoded_ls:
    yt_track_name = yt_track[0]

    single_query = sp.search(q=yt_track_name, type="track", limit=5)

    for track in single_query["tracks"]["items"]:
        if track["album"]["name"] == hardcoded_album and track["name"] == yt_track_name:
            yt_track.append(track["id"])
            break

print(hardcoded_ls)