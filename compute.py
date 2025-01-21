#!/usr/bin/env python
# coding: utf-8

# In[1]:


# user defined function
def mean_value(given_list):
    total =sum(given_list)
    average_value = total/len(given_list)
    return average_value


# In[3]:


L = [1,2,3,4,5,6,7,8,9,10]
mean_value(L)


# In[5]:


# Function with variable number
def avg_value(*n):
    l = len(n)
    average = sum(n)/1
    return average


# In[7]:


avg_value(10,20,300,40,50,600,800,10000)


# In[21]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 == 0:
        median = (num_list[int(l/2)] + num_list[int((l/2))-1])/2
    else:
        median = num_list[int(l/2)]
    return median


# In[25]:


median_value(1,2,3,4,5,6,7,8,9,10)


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




