#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np


# In[23]:


df = pd.read_csv("Universities.csv")
df


# In[25]:


# Mean value of SAT score
np.mean(df["SAT"])


# In[27]:


# Median of the data
np.median(df["SAT"])


# In[29]:


np.std(df["GradRate"])


# In[31]:


np.var(df["SFRatio"])


# In[33]:


df.describe()


# In[47]:


# visulize the gradRate usng 
import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


plt.hist(df["GradRate"])


# In[41]:


plt.figure()
plt.title("gradution Rate")
plt.hist(df["GradRate"])


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




