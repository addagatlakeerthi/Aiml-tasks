#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[5]:


#dir


# In[17]:


# create 1D numpy array
x = np.array([45,49,59,44,33,66,])
print(x)
print(type(x))
print(x.dtype)


# In[15]:


x = np.array([45,49,59,44,33,66,8.5])
print(x)
print(type(x))
print(x.dtype)


# In[19]:


# verify data type
x = np.array(["A",45,49,59,44,33,66,])
print(x)
print(type(x))
print(x.dtype)


# In[23]:


# create 2D numpy array 
a2 = np.array([[45,59],[44,66]])
print(a2)
print(type(a2))
print(a2.shape)


# In[25]:


# reshaping an array
a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[35]:


# create an array with arange()
c = np.arange(5,1000)
print(c)
type(c)


# In[39]:


# use of around()
d = np.array([1.2323, 4.4565, 4.56476])
print(d)
np.around(d,2)


# In[43]:


# create np.sqrt
d = np.array([1.2323, 4.4565, 4.56476,7.78986])
print(d)
print(np.around(np.sqrt(d),3))


# In[55]:


a1 = np.array([[3,4,5,8],[7,2,8,np.NaN]])
print(a1)
a1.dtype
                       


# In[63]:


# use of astype() to convert the data type
a1 = np.array([[3,4,5,8],[7,2,8,np.NaN]])
a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[73]:


a2 = np.array([[3,4,5,8],[7,2,81,12]])
a2


# In[75]:


a2 = np.array([[3,4,5,8],[7,2,81,12]])
a2.mean(axis=0)


# In[79]:


# matrix operations
a3 = np.array([[3,4,5,6],[7,8,9,7],[6,7,9,4]])
a3


# In[83]:


a3 = np.array([[3,4,5,6],[7,8,9,7],[6,7,9,4],[3,4,9,0]])
a3
np.fill_diagonal(a3,0)
print(a3)


# In[87]:


A = np.array([[1,2],[3,4]])
B = np.array([[7,6],[8,9]])
C = np.matmul(A,B)


# In[89]:


print(A.T)
print(B.T)


# In[93]:


# Accessing the array elements
a4 = np.array([[1,2,8],[3,4,5],[7,6,5],[4,8,9]])
a4              


# In[95]:


a4 = np.array([[1,2,8],[3,4,5],[7,6,5],[4,8,9]])
a4[2][0]


# In[97]:


a4 = np.array([[1,2,8],[3,4,5],[7,6,5],[4,8,9]])
a4[1:3][3:5]


# In[99]:


a4 = np.array([[1,2,8],[3,4,5],[7,6,5],[4,8,9]])
a4[1:3][3:]


# In[103]:


print(np.argmax(a3,axis=1))
print(np.argmax(a3,axis=1))


# In[105]:


# printvthe max value element
print(np.amax(a3,axis=1))
print(np.amax(a3,axis=1))


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




