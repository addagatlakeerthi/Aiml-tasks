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


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np 


# In[19]:


# Read the data from csv file
cars = pd.read_csv("Cars.csv")
cars.head()


# In[21]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# In[23]:


cars.info()


# In[25]:


#Description of columns
- MPG: Milege of the car(Mile per Gallon)(this is Y-column to be predicted)
- HP: Horse Power of the car(X1 column)
- VOL : Volume of the car(size)(X2 column)
- SP: Top speed of the car (Miles per Hour) (X3 column)
- WT : Weight of the car(Pounds) (X4 Column)


# In[27]:


# check for missing values
cars.isna().sum()


# In[29]:


Oservations about info() missing values
-There are no missing values
-There are 81 observations(81 different cars data)
-The data types of the columns are also relevant and valid


# In[31]:


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


# In[33]:


cars.corr()


# In[35]:


cars[cars.duplicated()]


# In[49]:


# pair plot
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[ ]:


Observations from correlation plots and coffcients
- B/w x and y, all the x variables are showing moderate to high correlation strengths, highest being b/w hp and mpg
-Therefore this dataset qualifies for building a multiple linear regression model to predict mpg
-Among x columns (x1,x2,x3,and x4), some very high correlation strenghts are observed b/w sp vs hp, vol vs wt
-The high corrrelation among x columns is not desirable as it might lead to multicollinearity problem


# In[51]:


# Build model
#import statsmodels.formula.api as smf
model1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[53]:


model1.summary()


# In[ ]:


y =b0+b1x1+b2x2+b3x3+b4x4
b0,b1,b2,b3,b4-model params or coefficients
1/2[e1,e2,e3,......] = mpg


# In[ ]:


Observations from model summary
- The R-squared and adjusted R-squared values are good and about 75% of variability in Y is explained by X columns
- The probability value with respect to F-statistic is close to zero, indicating that all or someoneof X columns are significant
- The p-value for VOL and WT are higher 5% indicating some interaction issue among themselves, which need to be further explored


# In[ ]:


performance metrics for model1


# In[55]:


# find the performance metrics
# create a data frame with actual y and predicted y columns
df1 = pd.DataFrame()
df1["actual_y1"] = cars["MPG"]
df1.head()


# In[57]:


# predict for the given X data columns
pred_y1 = model1.predict(cars.iloc[:,0:4])
df1["pred_y1"] = pred_y1
df1.head()


# In[ ]:





# In[ ]:





# In[ ]:




