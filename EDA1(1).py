#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


# printing the information 
data.info()


# In[4]:


# Dataframe attributes
print(type(data))
print


# In[5]:


data1 = data.drop(['Unnamed: 0', "Temp C"], axis =1)
data1


# In[6]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[7]:


# print all duplicated rows
data1[data1.duplicated(keep = False)]


# In[8]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[38]:


# change column nnames (rename the columns)
data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[44]:


data1.isnull().sum()


# In[42]:


cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[46]:


data1.info()


# In[10]:


#Display data1 info()
data1.info()


# In[11]:


# Display data1 missing values count in each column using isnull() .sum()
data1.isnull().sum()


# In[27]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean od Ozone: ", mean_ozone)


# In[29]:


data1['ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




