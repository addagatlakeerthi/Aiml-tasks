#!/usr/bin/env python
# coding: utf-8

# In[1]:


Asumptions in Multilinear Regression
1. Linearity: The relationship b/w the predictors(X) and the response(Y) is linear
2. Independence: Observations are independent of each other
3. Homoscedasticity: The residuals (Y-Y_hat) exbhit constant variance at all levels of the predictor
4. Normal Distribution Od Errors: The residuals of the model are naormally distributed
5. No Multicollinearity: The indepent variables should not be too highly correlated with each other.
violations of these assumptions may lead to inefficiency in the regression parameters and unreliable predictions.


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np 


# In[8]:


# Read the data from csv file
cars = pd.read_csv("Cars.csv")
cars.head()


# In[20]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# In[12]:


cars.info()


# In[ ]:


#Description of columns
- MPG: Milege of the car(Mile per Gallon)(this is Y-column to be predicted)
- HP: Horse Power of the car(X1 column)
- VOL : Volume of the car(size)(X2 column)
- SP: Top speed of the car (Miles per Hour) (X3 column)
- WT : Weight of the car(Pounds) (X4 Column)


# In[14]:


# check for missing values
cars.isna().sum()


# In[ ]:


Oservations about info() missing values
-There are no missing values
-There are 81 observations(81 different cars data)
-The data types of the columns are also relevant and valid


# In[18]:


# Create a fig with two subplots (one above the other)
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
# creating a boxplot
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')
# creating a histogram in the same x-axis
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
#Adjust layout
plt.tight_layout()
plt.show()


# In[ ]:


Observations from boxplot and histograms
- There are some extreme values (outliers) observed in towards the right tail of SP and HP distributons.
- In VOL and WT columns, a few outliers are observed in both tails of their distributions 
- The extreme values of cars data may have come from the specilaly designed nature of cars
- As this is multi-dimensional data, the outliers with respect to spatial dimensions may have to be considered while building the regression model


# In[22]:


cars.corr()


# In[26]:


cars[cars.duplicated()]


# In[24]:


# pair plot
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




