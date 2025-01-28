#!/usr/bin/env python
# coding: utf-8

# In[3]:


# load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# In[4]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[5]:


# printing the information 
data.info()


# In[6]:


# Dataframe attributes
print(type(data))
print


# In[7]:


data1 = data.drop(['Unnamed: 0', "Temp C"], axis =1)
data1


# In[8]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[9]:


# print all duplicated rows
data1[data1.duplicated(keep = False)]


# In[10]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[11]:


# change column nnames (rename the columns)
data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[12]:


data1.isnull().sum()


# In[13]:


cols = data1.columns
colors = ['black', 'yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[14]:


data1.info()


# In[15]:


#Display data1 info()
data1.info()


# In[16]:


# Display data1 missing values count in each column using isnull() .sum()
data1.isnull().sum()


# In[17]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean od Ozone: ", mean_ozone)


# In[18]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[19]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[20]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[21]:


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







# In[22]:


#### Observations box plot

-The ozone column has extreme values beyond 81 as seen from box plot 
-The same is confirmed from the below right-skewed  histogram
-out layers are extreme values


# In[ ]:


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


# In[25]:


plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"], vert= False)


# In[27]:


# Extract outliers from boxplot for ozone colmn
plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data1["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']] #fliers are outliers


# In[ ]:


##### Method 2
- using mu +/-3*sigma limits (Standard deviation method)


# In[29]:


data1["Ozone"].describe()


# In[31]:


mu = data1["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]

for x in data1["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[ ]:


Observations
* It is observed that only two outliers are identified using std  method  
*  In box plot method more no of outliers are identified
*  This is because the assumption of normality is not satified in this column


# In[33]:


import scipy.stats as stats
# Create Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(data1["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Dectection", fontsize=14)
plt.xlabel("Theoretical Quantile", fontsize=12)


# In[ ]:


## Observations from Q-Q plot
* The data does not follow normal distribution as the data points are deviting significantly away from the red line
* The dat shows a right-skewed ditribution and possible outliers


# In[35]:


# Create  a figure for violin plot
sns.violinplot(data=data1["Ozone"], color='lightgreen')
plt.title("Violin Plot")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





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




