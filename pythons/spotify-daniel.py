#!/usr/bin/env python
# coding: utf-8

# In[7]:


from __future__ import print_function
#Import things and whatnot.
import spotipy
from spotipy import Spotify
import requests
import json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

SPOTIFY_CLIENT_ID = '44e135d779674d7b9bec3daaea8a8f8d'
SPOTIFY_CLIENT_SECRET = '55f97cafaa874bb99d5d4d9e443312df'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'


# In[8]:


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


# In[106]:


#Pulls the tracks from a specific playlist
#Insert playlist id below
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'
playlist = 'spotify:user:spotifycharts:playlist:' + playlist_id
results = sp.playlist(playlist)

print(json.dumps(results, indent=4))


# In[107]:


#Returns the info of a specific track
#Insert the tracks id below
track_id = '11dFghVXANMlKmJXsNCbNl'
urn = 'spotify:track:' + track_id
track = sp.track(urn)

pprint(track)


# In[130]:


#Couldn't figure out the for loop but I assume it's easy for one of you geniuses :)

#for song in results['tracks']['items'][0]['track']['id']:
#    track = sp.track(song) 
#    print(song)


#In theory, that should work but tuples and lists are weird so ask a TA for me to get it all working ): Let me know if yall need anything else :)
results['tracks']['items'][0]['track']['id']


# In[ ]:




