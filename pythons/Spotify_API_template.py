#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[35]:


##read in csv or connect to url

# url = 'https://kworb.net/spotify/country/us_weekly_totals.html'
# table = pd.read_html(url)
# tbl = table[0]
# print(tbl.count())
# tbl


# In[12]:


###collect song names

###for url contained above:
# new = tbl["Artist and Title"].str.split(" - ", n = 1, expand = True)
# tbl["Track"]= new[1]
# tracks = tbl.iloc[:,8].values
# tracks
# for track in tracks:
#     track = str(track + ',')
#     print(track)

###for reading in csv
tracks = 'yourdf'.iloc[:,('target_column')].values


# In[8]:


###set up API

from __future__ import print_function
#Import things and whatnot.
import spotipy
from spotipy import Spotify
import requests
import json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

SPOTIFY_CLIENT_ID = '97d0cf2236334807b1eb85e357156547'
SPOTIFY_CLIENT_SECRET = '5daeca4781fb4ac98408b5ce82a01ff6'


SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'


# In[9]:


### Set up API part 2

#DONT TOUCH THIS ITS FROM SPOTIPY PROS NOT ME 
#https://github.com/plamere/spotipy/blob/51637d7b2c3f7ebcf12b94fd22d6fb21048949bc/spotipy/oauth2.py


__all__ = [
    'is_token_expired',
    'SpotifyClientCredentials',
    'SpotifyOAuth',
    'SpotifyOauthError'
]

import base64
import json
import os
import sys
import time

import requests

# Workaround to support both python 2 & 3
import six
import six.moves.urllib.parse as urllibparse


class SpotifyOauthError(Exception):
    pass


def _make_authorization_headers(client_id, client_secret):
    auth_header = base64.b64encode(
        six.text_type(
            client_id +
            ':' +
            client_secret).encode('ascii'))
    return {'Authorization': 'Basic %s' % auth_header.decode('ascii')}


def is_token_expired(token_info):
    now = int(time.time())
    return token_info['expires_at'] - now < 60

sp_oauth = oauth2.SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

class SpotifyClientCredentials(object):
    OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id=None, client_secret=None, proxies=None):
        """
        You can either provide a client_id and client_secret to the
        constructor or set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
        environment variables
        """
        if not client_id:
            client_id = SPOTIFY_CLIENT_ID

        if not client_secret:
            client_secret = SPOTIFY_CLIENT_SECRET

        if not client_id:
            raise SpotifyOauthError('No client id')

        if not client_secret:
            raise SpotifyOauthError('No client secret')

        self.client_id = client_id
        self.client_secret = client_secret
        self.token_info = None
        self.proxies = proxies

    def get_access_token(self):
        """
        If a valid access token is in memory, returns it
        Else feches a new token and returns it
        """
        if self.token_info and not self.is_token_expired(self.token_info):
            return self.token_info['access_token']

        token_info = self._request_access_token()
        token_info = self._add_custom_values_to_token_info(token_info)
        self.token_info = token_info
        return self.token_info['access_token']

    def _request_access_token(self):
        """Gets client credentials access token """
        payload = {'grant_type': 'client_credentials'}

        headers = _make_authorization_headers(
            self.client_id, self.client_secret)

        response = requests.post(self.OAUTH_TOKEN_URL, data=payload,
                                 headers=headers, verify=True,
                                 proxies=self.proxies)
        if response.status_code != 200:
            raise SpotifyOauthError(response.reason)
        token_info = response.json()
        return token_info

    def is_token_expired(self, token_info):
        return is_token_expired(token_info)

    def _add_custom_values_to_token_info(self, token_info):
        """
        Store some values that aren't directly provided by a Web API
        response.
        """
        token_info['expires_at'] = int(time.time()) + token_info['expires_in']
        return token_info
    
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


# In[13]:


### Make calls with API to extract song id's
####Warning, if you run this twice, it will append to the empty variables twice

all_dem_ids7 = []
record = 1
not_found = []
for track in tracks:
   try:
        song_id = sp.search(q=track, type='track', limit = 1)
        song = song_id["tracks"]['items'][0]['id']
        all_dem_ids7.append(song)
        for_log = song
        record= record + 1
        print(f"Processing Record {record}| {for_log}")
   except:
        not_found.append(record)
        print(f" id not found {record}")    


# In[46]:


##check length of returns

xy = len(all_dem_ids7)
xy

###check on rows to delete, minus one to get correct row to drop) 
to_drop = []
for x in not_found:
    drop = (x-1) 
    to_drop.append(drop)
to_drop


# In[50]:


###drop any rows where API didn't collect id numbers

spotify_tbl = tbl.drop(tbl.index[to_drop])


# In[51]:


###create empty lists, fill them with API call for audio features

track_id5 = []
dance5 = []
energy5 = []
key5 = []
loudness5 = []
mode5 = []
speechiness5 = []
acousticness5 = []
instrumentalness5 = []
liveness5 = []
valence5 = []
tempo5 = []
duration_ms5 = []
time_signature5 = []
record = 1
for features in all_dem_ids7:
   try:
        audio_analysis = sp.audio_features(features)
        track_id5.append(audio_analysis[0]['id'])
        dance5.append(audio_analysis[0]['danceability'])
        energy5.append(audio_analysis[0]['energy'])
        key5.append(audio_analysis[0]['key'])
        loudness5.append(audio_analysis[0]['loudness'])
        mode5.append(audio_analysis[0]['mode'])
        speechiness5.append(audio_analysis[0]['speechiness'])
        acousticness5.append(audio_analysis[0]['acousticness'])
        instrumentalness5.append(audio_analysis[0]['instrumentalness'])
        liveness5.append(audio_analysis[0]['liveness'])
        valence5.append(audio_analysis[0]['valence'])
        tempo5.append(audio_analysis[0]['tempo'])
        duration_ms5.append(audio_analysis[0]['duration_ms'])
        time_signature5.append(audio_analysis[0]['time_signature']) 
        record= record + 1
        print(f"Processing Record {record}")
        
   except:
        print("feat not Found")
        


# In[ ]:


###check lenght of returns
z = len(track_id5)
z


# In[207]:


####create dataframe for audio features

features = pd.DataFrame({'track_id' : track_id5,
                                     'danceability': dance5,
                                     'energy': energy5,
                                     'key': key5,
                                     'loudness': loudness5,
                                     'mode' : mode5,
                                     'speechiness' : speechiness5,
                                     'acousticness' : acousticness5,
                                     'instrumentalness': instrumentalness5,
                                     'liveness': liveness5,
                                     'valence': valence5,
                                     'tempo':tempo5,
                                     'duration_ms': duration_ms5,
                                     'time_signature': time_signature5}
                                    )
features 


# In[ ]:


#add list of track ids to first data set
spotify_tbl['track_id'] = all_dem_ids7


# In[206]:


###combine dataframes
top_hits = pd.merge(spotify_tbl,features, on = "track_id")

###load combined dataframe to csv
top_hits.to_csv('top_hits_2007-2020.csv', index=False)

