#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

SPOTIFY_CLIENT_ID = '97d0cf2236334807b1eb85e357156547'

SPOTIFY_CLIENT_SECRET = '5daeca4781fb4ac98408b5ce82a01ff6'

token = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                 client_secret=SPOTIFY_CLIENT_SECRET)

cache_token = token.get_access_token()

spotify = Spotify(cache_token)


# In[2]:


import spotipy

#__init__(auth= cache_token, requests_session=True, client_credentials_manager=token, proxies=None, requests_timeout=None)

util.prompt_for_user_token(username,scope,client_id='97d0cf2236334807b1eb85e357156547',client_secret='5daeca4781fb4ac98408b5ce82a01ff6',redirect_uri='your-app-redirect-url')

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)


# In[3]:


specific_time = requests.get(featured_playlists(locale=None, country=None, timestamp='2020-01-23 12:33:54', limit=20, offset=0)).json()
print(specific_time)


# In[ ]:




