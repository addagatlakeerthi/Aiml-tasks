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


# In[16]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[17]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[18]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[19]:


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







# In[20]:


#### Observations box plot

-The ozone column has extreme values beyond 81 as seen from box plot 
-The same is confirmed from the below right-skewed  histogram
-out layers are extreme values


# In[26]:


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


# In[27]:


plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"], vert= False)


# In[ ]:


# Extract outliers from boxplot for ozone colmn
plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data1["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']] #fliers are outliers


# In[ ]:


##### Method 2
- using mu +/-3*sigma limits (Standard deviation method)


# In[ ]:


data1["Ozone"].describe()


# In[30]:


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


# In[ ]:


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


# In[32]:


# Create  a figure for violin plot
sns.violinplot(data=data1["Ozone"], color='lightgreen')
plt.title("Violin Plot")
# Show the plot
plt.show()


# In[34]:


sns.swarmplot(data=data1, x = "Weather", y = "Ozone",color="orange",palette="Set2", size=6)


# In[36]:


sns.stripplot(data=data1, x = "Weather", y = "Ozone",color="orange",palette="Set2", size=6)


# In[38]:


sns.kdeplot(data=data1["Ozone"], fill=True, color="blue")
sns.rugplot(data=data1["Ozone"], color="black")


# In[40]:


sns.boxplot(data = data1, x = "Weather", y = "Ozone")


# In[44]:


#Correlation coefficient and pair plots
plt.scatter(data1["Wind"], data1["Temp"])


# In[46]:


# Compute pearson correlation coefficient
data1["Wind"].corr(data1["Temp"])


# In[ ]:


#### Observation
- The observation   between wind and temp is observed to be negatively correlated with mild strength 


# In[48]:


# Read all numeric (float) colums into a new table data1_nummeric
data1_numeric = data1.iloc[:,[0,1,2,6]]
data1_numeric


# In[50]:


data1.head()


# In[52]:


# print correlation coeffcienys foe all the above columns
data1_numeric.corr()


# In[ ]:


-Highest corrrelation produce  between ozone and temperture (0.59)
-Next higher correlation observe between ozone and wind (-0.523738	) 
-Next higher correlation observe between wind and temperture (0.441228)
- The least correlation strength  is obserb=ved b/w solar and wind (-0.055
874)


# In[60]:


# plot a pair b/w all numeric colums using seaborn
sns.pairplot(data1_numeric)


# In[ ]:


Transformations


# In[62]:


#Creating Dummy variable for weather column
data2=pd.get_dummies(data1,columns=['Month', 'Weather'])
data2


# In[ ]:


######## Normalization


# In[64]:


data1_numeric.values


# In[70]:


# Normalization of the data
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
array = data1_numeric.values
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(array)
#transformed data
set_printoptions(precision=2)
print(rescaledX[0:10,:])


# In[ ]:




