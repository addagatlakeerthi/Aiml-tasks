#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = 6 
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[7]:


x = 10
result = "postive" if x > 0 else "Negative"
print(result)


# In[5]:


age = 18
category = "Adult" if age >= 18 else "Mionr"
print(category)


# In[13]:


num = 0 
result = "Postive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)


# In[19]:


#list comprehension
L =[1,3,7,8,9]
[2*x for x in L]


# In[23]:


L =[12,93,76,81,8]
[2/x for x in L]


# In[42]:


L =[12,93,76,81,87,99,66,5]
[x for x in L if x%2 == 0]


# In[44]:


[x for x in L if x%2 != 0]


# In[49]:


# dict comprehension
d1 = {'Ram':[22,3,44,55,66], 'krishna':[33,77,99,88], 'prem':[99,3,6,77,8]}
d1


# In[53]:


{k:sum(v)/len(v) for k,v in d1.items()}


# In[67]:


# user defined function
def mean_value(given_list):
    total =sum(given_list)
    average_value = total/len(given_list)
    return average_value


# In[69]:


L = [1,2,3,4,5,6,7,8,9,10]
mean_value(L)


# In[75]:


def greet(name):
    print(f"Good Morning, {name}!")
greet("keerthi")

    


# In[8]:


# Function with variable number
def avg_value(*n):
    l = len(n)
    average = sum(n)/1
    return average


# In[14]:


avg_value(10,20,300,40,50,600,800,10000)


# In[ ]:


Lambda Function


# In[26]:


greet = lambda name : print(f"Have a nice day {name}!")


# In[28]:


greet("keerthi")


# In[ ]:


write a lambda Function to print the product of three numbers


# In[36]:


product = lambda a,b,c : a*b*c
product(20,30,40)


# In[38]:


even = lambda L : [x for x in L if x%2 ==0]


# In[40]:


my_list = [100,3,5,7,88,99,90]
even(my_list)


# In[42]:


odd = lambda L : [x for x in L if x%2 ==0]


# In[44]:


my_list = [100,3,5,7,88,99,90]
odd(my_list)


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




