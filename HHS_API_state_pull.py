
# coding: utf-8

# # Class: USC Viterbi Data Analytics Bootcamp
# 
# Team: Analyticus (aka Team 5)
# 
# Module: pull_flu_data_Flutrack
# 
# Input: HHS Vaccination API data pull
# 
# Output: hhs_state.json
#     
# 
# Description: Vaccination counts and percentages by state
# 

# In[ ]:


# Dependencies
import requests
import json
import numpy as np
import pandas as pd


# In[ ]:


#Source
# URL for GET requests to retrieve vehicle data\n",
url = "https://fluvaccineapi.hhs.gov/api/v2/ids/2017/states.json"


# In[ ]:


# Create the lsit of state codes, removing Distict of Columbia and Puerto Rico.
# Analysis will only include continental 50 states
state_codes = requests.get(url).json()
state_codes.remove('DC')
state_codes.remove('PR')


# In[ ]:


print(requests.get(url))


# In[ ]:


#Retrieving data and converting it into JSON\n",
print(requests.get(url).json())


# In[ ]:


state_codes = requests.get(url).json()
print(state_codes)


# In[ ]:


state_dict = {}
state_index = 0
    
    for state_code in state_codes:

        url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/states/{}.json?ethnicity=T&medicare_status=A\".format(state_code)
        state_list = requests.get(url).json()
        
        for i in np.arange(0, len(state_list)):
            state_dict[str(state_index)] = state_list[i]
            print(state_list[i])
            state_index += 1
            print(requests.get(url).json())


# In[ ]:


# Build a list of state vaccination data.
results = []

for state_code in state_codes:
    
    url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/2017/states/{}.json?ethnicity=T&medicare_status=A".format(state_code)
    
    state_list = requests.get(url).json()
    
    for i in np.arange(0, len(state_list)):
        results.append(state_list[i])


# In[ ]:


# Load a dataframe with the HHS data.
df = pd.DataFrame(results)
df = pd.DataFrame.from_dict(state_dict)


# In[ ]:


df = df.T
df2 = df.sort_values(by=['year', 'week'])
df2.head()


# In[ ]:


df3 = df2[['short_name','count', 'percentage', 'week']]
df4 = df3.rename(columns={short_name: "state", count:"vaccinations", percentage:"vac_percent"})\n",
df4.head()


# In[ ]:


HHS_state = df4.to_json(orient='records')[1:-1].replace('},{', '} {')


# In[ ]:


with open('HHS_state.txt', 'w') as f:,
    f.write(HHS_state)


# In[ ]:




