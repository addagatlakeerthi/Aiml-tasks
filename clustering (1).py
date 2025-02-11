#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans


# In[14]:


Univ = pd.read_csv("Universities.csv")
Univ


# In[16]:


Univ.describe()


# In[18]:


# Read all numeric columns in to Univ1
Univ1 = Univ.iloc[:,1:] 


# In[20]:


Univ1


# In[22]:


Univ1.columns


# In[42]:


cols = Univ1.columns


# In[44]:


# Standardisation function
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1),columns = cols )
scaled_Univ_df
#Scaler.fit_transform(Univ1)


# In[46]:


from sklearn.cluster import KMeans 
clusters_new = KMeans(3, random_state=0)
clusters_new.fit(scaled_Univ_df)


# In[48]:


clusters_new.labels_


# In[50]:


set(clusters_new.labels_)


# In[58]:


#Univ['clusterid_new'] = clusters_new.labels_


# In[62]:


Univ.sort_values(by = "clusterid_new")


# In[64]:


Univ.iloc[:,1:].groupby("clusterid_new").mean()


# In[ ]:


"I’ll keep track of our deadlines."
"Let’s set reminders so we don’t miss anything."
"I’ll let you know if we’re running out of time."


# In[ ]:


Observations 
-Cluster 2 appears to be the top rated universities cluster as the cut off score,Top 10, SFratio parameter mean values are high
-Cluster 1 appears to occupy the middle level rated universitites
-Cluster 0 comes as the lower level rated universities


# In[66]:


Univ[Univ['clusterid_new']==0]


# In[70]:


wcss = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i,random_state=0 )
    kmeans.fit(scaled_Univ_df)
    #kmeans.fit(Univ1)
    wcss.append(kmeans.inertia_)
print(wcss)
plt.plot(range(1, 20), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
    


# In[ ]:


## observations
from the above graph we can choose k=3 or 4 which indicates elbow join that is the rate of change of slop dicreases


# In[ ]:


Clustering Methods:
1.hierarcial clustering
2.K means clustering
3.k medoids clustering
4.k prototype clustering
5.DB SCAN


# In[ ]:





# In[ ]:




