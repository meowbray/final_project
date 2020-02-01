#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[136]:


url = 'https://kworb.net/spotify/country/us_weekly_totals.html'
table = pd.read_html(url)
tbl = table[0]
# c =tbl.loc[324]
# c
print(tbl.count())
tbl


# In[235]:


dupes = tbl.pivot_table(index=['Artist and Title'], aggfunc='size')
dupes

any_dupes = tbl['Artist and Title'].duplicated().any() 
any_dupes

# for g in dupes:
#     print(g)
    
no_dupes = tbl.drop_duplicates('Artist and Title', keep = 'first')
no_dupes


# In[236]:


new = tbl["Artist and Title"].str.split(" - ", n = 1, expand = True)
tbl["Track"]= new[1]
tracks = tbl.iloc[:,8].values
tracks

# for track in tracks:
#     track = str(track + ',')
#     print(track)


# In[137]:


tbl.to_csv('songs_top200_07_20.csv', index=False)


# In[ ]:





# In[237]:


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


# In[ ]:





# In[238]:


# -*- coding: utf-8 -*-

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


# In[216]:


top200_spotify = tbl.drop(tbl.index[[324,359,1637,2730,2840,2964,3082,3376,3390,3716,3911,4026,4115,4248,4265,4312,4436,4494,4622,4635,4650,4651]])
# e = tbl.iloc[324,:]
# e
# top200_spotify.head(50)


# In[240]:


all_dem_ids6 = []
record = 1
# not_found = []
for track in tracks:
   try:
        song_id = sp.search(q=track, type='track', limit = 1)
        song = song_id["tracks"]['items'][0]['id']
        all_dem_ids6.append(song)
        for_log = song
        record= record + 1
        print(f"Processing Record {record}| {for_log}")
   except:
        print(f" id not found {record}")    


# In[241]:


xy = len(all_dem_ids6)
xy


# 

# In[31]:


# broken_id = sp.search(q='despicito', type='track', limit = 2)
# broken_id2 = broken_id["tracks"]['items'][0]['id']
# broken_id2


# In[ ]:


ad = sp.audio_features()


# In[187]:


# all_dem_features = []
# for features in all_dem_ids3:
#    try:
#         audio_analysis = sp.audio_features(features)
#         all_dem_features.append(audio_analysis)
#         for_log = feat
#         print(f"Processing Record | {feat}")
#    except:
#         print("feat not Found")
#         time.sleep(1.7)


# In[202]:


all_dem_ids3


# In[205]:


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
for features in all_dem_ids4:
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
        


# In[189]:





# In[147]:


feat = sp.audio_features('7tvuLLroI0n6uYBWuFig5d')
# audio_df = pd.DataFrame.from_dict(feat)
# audio_df
feat[0]['id']


# In[207]:


top200_features = pd.DataFrame({'track_id' : track_id5,
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
top200_features 


# In[222]:


boolean = top200_features['track_id'].duplicated().any() 
boolean

x = top200_features.pivot_table(index=['track_id'], aggfunc='size')

top200_features.drop_duplicates()


# In[ ]:





# In[224]:


top200_spotify


# In[225]:


y = top200_spotify.pivot_table(index=['Track'], aggfunc='size')
for y in y:
   print(y)


# In[99]:



# featured = pd.DataFrame.from_dict(dem_features)

# stuff = []
# for x,y in featured:
#     thing = featured.iloc[x:][y:]
#     stuff.append(thing)
    
# stuff2 = pd.DataFrame.from_dict(stuff)
# stuff2

# featured


# for index in range(len(all_dem_features)):
#     for key in all_dem_features[index]:
#         print(all_dem_features[index][key])
# b = featured.series.apply(featured)
# b
all_dem_features


# In[206]:



# dance = []
# energy = []
# key = []
# loudness = []
# mode = []
# speechiness = []
# acousticness = []
# instrumentalness = []
# liveness = []
# valence = []
# tempo = []
# duration_ms = []
# time_signature = []


# for feature_data in range(1,4831):
#     d = all_dem_features[feature_data][0]['danceability']
#     dance.append(d)
#     e =all_dem_features[feature_data][0]['energy']
#     energy.append(e)
#     k =all_dem_features[feature_data][0]['key']
#     key.append(k)
#     l =all_dem_features[feature_data][0]['loudness']
#     loudness.append(l)
#     m =all_dem_features[feature_data][0]['mode']
#     mode.append(m)
#     s =all_dem_features[feature_data][0]['speechiness']
#     speechiness.append(s)
#     a =all_dem_features[feature_data][0]['acousticness']
#     acousticness.append(a)
#     i =all_dem_features[feature_data][0]['instrumentalness']
#     instrumentalness.append(i)
#     l =all_dem_features[feature_data][0]['liveness']
#     liveness.append(l)
#     v =all_dem_features[feature_data][0]['valence']
#     valence.append(v)
#     t =all_dem_features[feature_data][0]['tempo']
#     tempo.append(t)
#     dr =all_dem_features[feature_data][0]['duration_ms']
#     duration_ms.append(dr)
#     tm =all_dem_features[feature_data][0]['time_signature']
#     time_signature.append(tm)


# In[130]:


features_top200_07_20 = pd.DataFrame({'danceability': dance,
                                     'energy': energy,
                                     'key': key,
                                     'loudness': loudness,
                                     'mode' : mode,
                                     'speechiness' : speechiness,
                                     'acousticness' : acousticness,
                                     'instrumentalness': instrumentalness,
                                     'liveness': liveness,
                                     'valence': valence,
                                     'tempo':tempo,
                                     'duration_ms': duration_ms,
                                     'time_signature': time_signature}
                                    )
features_top200_07_20


# In[131]:


features_top200_07_20.to_csv('features_top200_07_20.csv', index=False)


# In[134]:


features_top200_07_20.count()


# In[214]:


# frames = [top200_spotify, top200_features]
# top200 = pd.concat(frames)
# top200


# In[ ]:




