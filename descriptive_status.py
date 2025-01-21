#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Universities.csv")
df


# In[6]:


# Mean value of SAT score
np.mean(df["SAT"])


# In[8]:


# Median of the data
np.median(df["SAT"])


# In[10]:


np.std(df["GradRate"])


# In[12]:


np.var(df["SFRatio"])


# In[14]:


df.describe()


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




