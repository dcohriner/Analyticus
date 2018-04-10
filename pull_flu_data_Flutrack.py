
# coding: utf-8

# # Class: USC Viterbi Data Analytics Bootcamp
# 
# Team: Analyticus (aka Team 5)
# 
# Module: pull_flu_data_Flutrack
# 
# Input: CDC Influenza-Like-Illness CSV File
# 
# Output: cdc.json
#     
# Search terms = ["Influenza", "flu", "chills", "headache", "sore throat", "runny nose", "sneezing", "fever", "dry cough"]
# 
# Time Range: Week 40 2017 (October 2, 2017) to Week 11 2018 (March 18, 2018)
# 
# Description:
# 
# Load pandas.DataFrame from cdc.csv file.
# Format json string by looping through the DataFrame
# Write json string to cdc.json

# In[25]:


# Dependencies
import numpy as np
import pandas as pd
import time
from urllib.parse import urlparse
from pprint import pprint
import requests



# In[28]:


# Request articles
flu_track_mainAPI = 'http://api.flutrack.org/?time=500'
print(requests.get(flu_track_mainAPI))

#tweet_date = '175'
#url = flu_track_mainAPI + urllib.parse.urlencode({'tweet_date': tweet_date})

#json_data = requests.get(url).json()


# In[29]:


print(requests.get(flu_track_mainAPI).json())


# In[ ]:


# Request articles
tweets = requests.get(flu_track_url).json()

# The "response" property in articles contains the actual tweets
# list comprehension.
articles_list = [tweets for tweets in articles["response"]["docs"]]
pprint(articles_list)


# In[5]:


# Load pandas.Dataframe from cdc.csv.
#df = pd.read_csv('cdc.csv')


# In[8]:


# Format string to be suitable for a json file.
cases_str = str(cases_dict)
cases_str = cases_str.replace("'", '"')


# In[9]:


# Inspect resulting string.
# cases_str


# In[10]:


# Write string to cdc.json
with open('cdc.json', 'w') as f:
    f.write(cases_str)

