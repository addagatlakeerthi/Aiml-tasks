#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv("Universities.csv")
df


# In[9]:


# Mean value of SAT score
np.mean(df["SAT"])


# In[11]:


# Median of the data
np.median(df["SAT"])


# In[13]:


np.std(df["GradRate"])


# In[15]:


np.var(df["SFRatio"])


# In[17]:


df.describe()


# In[19]:


# visulize the gradRate usng 
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


plt.hist(df["GradRate"])


# In[21]:


plt.figure()
plt.title("gradution Rate")
plt.hist(df["GradRate"])


# In[ ]:





# In[28]:


#Visulation using boxplot
s = [20,10,30,40,50,70,60,99,55,45]
scores = pd.Series(s)
scores


# In[32]:


plt.boxplot(scores, vert=False)


# In[44]:


s = [120,100,300]
scores = pd.Series(s)
scores


# In[46]:


plt.boxplot(scores, vert=False)


# In[56]:


s = [20,30]
scores = pd.Series(s)
scores


# In[58]:


plt.boxplot(scores, vert=False)


# In[60]:


# outliers in universities datasets
df = pd.read_csv("universities.csv")
df


# In[63]:


plt.figure(figsize=(6,2))
plt.title("Box plot for SAT Score")
plt.boxplot(df["SAT"], vert = False)


# In[65]:


plt.figure(figsize=(9,2))
plt.title("Box plot for SAT Score")
plt.boxplot(df["SAT"], vert = False)


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




