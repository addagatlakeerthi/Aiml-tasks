#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


# In[3]:


iris = pd.read_csv("iris.csv")
print(iris)


# In[33]:


iris.info()


# In[35]:


iris.describe()


# In[37]:


iris.head()


# In[39]:


iris.isnull()


# In[44]:


labelencoder = LabelEncoder()
iris.iloc[:, -1] = labelencoder.fit_transform(iris.iloc[:, -1])


# In[46]:


iris


# In[ ]:




