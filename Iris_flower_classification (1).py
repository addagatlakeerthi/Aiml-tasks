#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


# In[4]:


iris = pd.read_csv("iris.csv")
print(iris)


# In[5]:


iris.info()


# In[6]:


iris[iris.duplicated(keep= False)]


# In[7]:


iris.describe()


# In[8]:


iris.head()


# In[9]:


iris.isnull()


# In[10]:


labelencoder = LabelEncoder()
iris.iloc[:, -1] = labelencoder.fit_transform(iris.iloc[:, -1])


# In[11]:


iris


# In[26]:


iris['variety'] = pd.to_numeric(labelencoder.fit_transform(iris['variety']))
print(iris.info())


# In[32]:


X=iris.iloc[:,0:4]
Y=iris['variety']


# In[46]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state = 1)
x_train


# In[48]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
x_train


# In[54]:


model = DecisionTreeClassifier(criterion = 'entropy',max_depth =None)
model.fit(x_train,y_train)


# In[56]:


plt.figure(dpi=1200)
tree.plot_tree(model);


# In[ ]:




