#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[31]:


df = pd.read_csv("top_hits_2007-2020.csv")
# Drop the null columns where all values are null
# df = df.dropna(axis='columns', how='all')
# Drop the null rows
data=df.drop(columns=["Artist and Title", ""'(x?)'"",'Track','track_id'])

audio_only = data.fillna(0)
audio_only


# In[42]:


X = audio_only.drop("mode", axis = 1)
y = audio_only["mode"]

###use this for _featureimportances function with Random Forest
feature_names = audio_only.columns


# In[43]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[44]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(X_train, y_train)
rf.score(X_test, y_test)


# In[45]:


sorted(zip(rf.feature_importances_, feature_names), reverse=True)


# In[48]:


import joblib
filename = 'Clay.sav'
joblib.dump(rf, filename)

