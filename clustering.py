#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans


# In[12]:


Univ = pd.read_csv("Universities.csv")
Univ


# In[15]:


Univ.describe()


# In[17]:


# Read all numeric columns in to Univ1
Univ1 = Univ.iloc[:,1:] 


# In[19]:


Univ1


# In[33]:


Univ1.columns


# In[29]:


# Standardisation function
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1),columns = cols )
scaled_Univ_df
#Scaler.fit_transform(Univ1)


# In[ ]:





# In[ ]:




