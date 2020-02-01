#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("top_hits_2007-2020.csv")
# Drop the null columns where all values are null
# df = df.dropna(axis='columns', how='all')
# Drop the null rows
data=df.drop(columns=["Artist and Title", ""'(x?)'"",'Track','track_id'])

audio_only = data.fillna(0)
audio_only


# In[7]:


X = audio_only.drop("Total", axis = 1)
y = audio_only["Total"]

###use this for _featureimportances function with Random Forest
feature_names = audio_only.columns
print("Shape", X.shape, y.shape)
y = y.values.reshape(-1,1)
y
print("Shape", X.shape, y.shape)


# In[8]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[ ]:





# In[9]:



from sklearn.linear_model import LinearRegression

### BEGIN SOLUTION

model = LinearRegression()


# In[10]:


model.fit(X, y)
training_score = model.score(X_train, y_train)
testing_score = model.score(X_test, y_test)

print(f"Training Score: {training_score}")
print(f"Testing Score: {testing_score}")


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.scatter(model.predict(X_train), model.predict(X_train) - y_train, c="blue", label="Training Data")
plt.scatter(model.predict(X_test), model.predict(X_test) - y_test, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y.min(), xmax=y.max())
plt.title("Residual Plot")


# In[12]:


y_predicted = model.predict(X_test)


# In[13]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm


# In[ ]:



        


# In[ ]:




