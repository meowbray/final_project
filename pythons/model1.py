#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Update sklearn to prevent version mismatches
get_ipython().system('pip install sklearn --upgrade')


# In[2]:


# install joblib. This will be used to save your model. 
# Restart your kernel after installing 
get_ipython().system('pip install joblib')


# In[65]:


import pandas as pd
import matplotlib.pyplot as plt


# # Read the CSV and Perform Basic Data Cleaning

# In[66]:


df = pd.read_csv("exoplanet_data.csv")
# Drop the null columns where all values are null
df = df.dropna(axis='columns', how='all')
# Drop the null rows
df = df.dropna()
df
print(df.columns.values)


# # Select your features (columns)

# In[71]:


# Set features. This will also be used as your x values.
X = df[['koi_period', 'koi_period_err1', 'koi_period_err2',
 'koi_time0bk', 'koi_time0bk_err1' ,'koi_time0bk_err2' ,'koi_impact',
 'koi_impact_err1', 'koi_impact_err2' ,'koi_duration', 'koi_duration_err1',
 'koi_duration_err2', 'koi_depth' ,'koi_depth_err1' ,'koi_depth_err2',
 'koi_prad', 'koi_prad_err1' ,'koi_prad_err2' ,'koi_teq', 'koi_insol',
 'koi_insol_err1' ,'koi_insol_err2' ,'koi_model_snr', 'koi_tce_plnt_num',
 'koi_steff', 'koi_steff_err1' ,'koi_steff_err2' ,'koi_slogg',
 'koi_slogg_err1' ,'koi_slogg_err2', 'koi_srad', 'koi_srad_err1',
 'koi_srad_err2' ,'ra', 'dec', 'koi_kepmag']]
y = df["koi_disposition"]

feature_names = df.columns


# # Create a Train Test Split
# 
# Use `koi_disposition` for the y values

# In[72]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)


# In[57]:


# from sklearn.ensemble import RandomForestClassifier
# rf = RandomForestClassifier(n_estimators=200)
# rf = rf.fit(X_train, y_train)
# rf.score(X_test, y_test)


# In[69]:


# sorted(zip(rf.feature_importances_, feature_names), reverse=True)


# # Pre-processing
# 
# Scale the data using the MinMaxScaler and perform some feature selection

# In[73]:


from sklearn.preprocessing import LabelEncoder, MinMaxScaler

X_scaler = MinMaxScaler().fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)



# # Train the Model
# 
# 

# In[74]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train_scaled, y_train)
print(f"Training Data Score: {model.score(X_train_scaled, y_train)}")
print(f"Testing Data Score: {model.score(X_test_scaled, y_test)}")


# # Hyperparameter Tuning
# 
# Use `GridSearchCV` to tune the model's parameters

# In[60]:


from sklearn.model_selection import GridSearchCV
param_grid = {'C': [1, 5, 10, 50],
              'gamma': [0.0001, 0.0005, 0.001, 0.005]}
grid = GridSearchCV(model, param_grid, verbose=3)


# In[61]:


grid.fit(X_train_scaled, y_train)# Train the model with GridSearch


# In[62]:


print(grid.best_params_)
print(grid.best_score_)


# # Save the Model

# In[ ]:


# save your model by updating "your_name" with your name
# and "your_model" with your model variable
# be sure to turn this in to BCS
# if joblib fails to import, try running the command to install in terminal/git-bash
import joblib
filename = 'your_name.sav'
joblib.dump(your_model, filename)

