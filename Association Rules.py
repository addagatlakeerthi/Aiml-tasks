#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install mlxtend library
get_ipython().system(' pip install mlxtend')


# In[8]:


# Import necessary libraries
import pandas as pd
import mlxtend 
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt


# In[10]:


# print the dataframe
titanic = pd.read_csv("Titanic.csv")
titanic


# In[12]:


titanic.info()


# In[ ]:


# Observations
- There are no null values
- All columns objects are datatype & categorical in natural 
- As the columns are categorical, we can adopt one-hot-encoding


# In[16]:


# plot a bar to visualize the category of people on the ship
counts = titanic['Class'].value_counts()
plt.bar(counts.index, counts.values)


# In[20]:


# plot a bar to visualize the category of people on the ship
counts = titanic['Gender'].value_counts()
plt.bar(counts.index, counts.values)


# In[22]:


# Perform onehot encoding on categorical columns
df=pd.get_dummies(titanic,dtype=int)
df.head()


# In[24]:


df.info()


# In[28]:


# Apply Apriori alogorithm to get itemset  
frequent_itemsets = apriori(df, min_support = 0.05,use_colnames=True,max_len=None)
frequent_itemsets


# In[30]:


frequent_itemsets.info()


# In[32]:


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
rules


# In[34]:


rules.sort_values(by='lift', ascending =True)


# In[44]:


import matplotlib.pyplot as plt
rules[['support', 'confidence','lift']].hist(figsize=(15,7))
plt.show()


# In[ ]:




