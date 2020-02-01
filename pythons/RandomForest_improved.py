#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("top_hits_2007-2020.csv")
# Drop the null columns where all values are null
# df = df.dropna(axis='columns', how='all')
# Drop the null rows
data=df.drop(columns=["Artist and Title", ""'(x?)'"",'Track','track_id', "Pos", "Wks","T10","Pk","PkStreams"])

audio_only = data.fillna(0)
audio_only


# In[5]:


plt.hist(audio_only.iloc[:,0], bins=8)
plt.ylabel("Songs in Category", fontsize=16)
plt.xlabel("Number of Streams in Millions", fontsize=16)
plt.title("Categories of Streams", fontsize=20)
plt.show()


# In[6]:


def f(row):
    if row["Total"] < 999999:
        val = 1
    elif row["Total"] > 1000000 and row["Total"] < 39999999:
        val = 2
    elif row["Total"] > 40000000 and row["Total"] < 79999999:
        val = 3
    elif row["Total"] >  80000000 and row["Total"] < 119999999:
        val = 4
    elif row["Total"] > 120000000 and row["Total"] < 159999999:
        val = 5
    elif row["Total"] > 160000000 and row["Total"] < 199999999:
        val = 6
    else:
        val = 7
    return val


# In[7]:


audio_only['Stream Category'] = audio_only.apply(f, axis=1)
audio_only.head()


# In[8]:


vc = audio_only["Stream Category"].value_counts()
vc


# In[26]:


processed=audio_only.drop(columns=["Total"])


# In[10]:


X = processed.drop("Stream Category", axis = 1)
y = processed["Stream Category"]

###use this for _featureimportances function with Random Forest
feature_names = audio_only.columns


# In[11]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[24]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=300)
rf = rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))
print(rf.score(X_train, y_train))


# In[13]:


sorted(zip(rf.feature_importances_, feature_names), reverse=True)


# In[ ]:




