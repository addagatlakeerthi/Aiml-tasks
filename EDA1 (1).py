#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


# printing the information 
data.info()


# In[4]:


# Dataframe attributes
print(type(data))
print


# In[5]:


data1 = data.drop(['Unnamed: 0', "Temp C"], axis =1)
data1


# In[6]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[7]:


# print all duplicated rows
data1[data1.duplicated(keep = False)]


# In[8]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[9]:


# change column nnames (rename the columns)
data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[10]:


data1.isnull().sum()


# In[11]:


cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[12]:


data1.info()


# In[13]:


#Display data1 info()
data1.info()


# In[14]:


# Display data1 missing values count in each column using isnull() .sum()
data1.isnull().sum()


# In[15]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean od Ozone: ", mean_ozone)


# In[141]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[143]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[147]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[157]:


#Detection of outliers in the columns
fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})
sns.boxplot(data=data1["Ozone"], ax=axes[0], color='skyblue', width=0.5, orient ='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")
# plot the boxplot in the frist (top)
sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[0].set_ylabel("Frequency")
#Ajust layout for better spacing 
plt.tight_layout()
# show the plot
plt.show()







# In[ ]:


#### Observations box plot

-The ozone column has extreme values beyond 81 as seen from box plot 
-The same is confirmed from the below right-skewed  histogram
-out layers are extreme values


# In[159]:


# Sample DataFrame creation (replace with your solar data)
data = {
    'solar': [3.2, 4.5, 5.6, 6.1, 7.0, 5.5, 6.3, 7.4, 3.8, 6.9, 4.8, 5.3, 6.0, 4.9, 5.7]
}
df = pd.DataFrame(data)

# Set up the figure for subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Boxplot
sns.boxplot(data=df, x='solar', ax=axes[0])
axes[0].set_title('Boxplot of Solar Data')
axes[0].set_xlabel('Solar Energy')

# Histogram
sns.histplot(df['solar'], bins=10, kde=True, ax=axes[1])
axes[1].set_title('Histogram of Solar Data')
axes[1].set_xlabel('Solar Energy')
axes[1].set_ylabel('Frequency')

# Show the plot
plt.tight_layout()  # Adjusts spacing between plots
plt.show()


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


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


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




