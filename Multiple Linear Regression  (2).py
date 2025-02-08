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


# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np 


# In[35]:


# Read the data from csv file
cars = pd.read_csv("Cars.csv")
cars.head()


# In[36]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# In[37]:


cars.info()


# In[38]:


#Description of columns
- MPG: Milege of the car(Mile per Gallon)(this is Y-column to be predicted)
- HP: Horse Power of the car(X1 column)
- VOL : Volume of the car(size)(X2 column)
- SP: Top speed of the car (Miles per Hour) (X3 column)
- WT : Weight of the car(Pounds) (X4 Column)


# In[40]:


# check for missing values
cars.isna().sum()


# In[42]:


Oservations about info() missing values
-There are no missing values
-There are 81 observations(81 different cars data)
-The data types of the columns are also relevant and valid


# In[44]:


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


# In[46]:


cars.corr()


# In[48]:


cars[cars.duplicated()]


# In[ ]:


# pair plot
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[51]:


Observations from correlation plots and coffcients
- B/w x and y, all the x variables are showing moderate to high correlation strengths, highest being b/w hp and mpg
-Therefore this dataset qualifies for building a multiple linear regression model to predict mpg
-Among x columns (x1,x2,x3,and x4), some very high correlation strenghts are observed b/w sp vs hp, vol vs wt
-The high corrrelation among x columns is not desirable as it might lead to multicollinearity problem


# In[ ]:


# Build model
#import statsmodels.formula.api as smf
model1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[55]:


model1.summary()


# In[57]:


y =b0+b1x1+b2x2+b3x3+b4x4
b0,b1,b2,b3,b4-model params or coefficients
1/2[e1,e2,e3,......] = mpg


# In[59]:


Observations from model summary
- The R-squared and adjusted R-squared values are good and about 75% of variability in Y is explained by X columns
- The probability value with respect to F-statistic is close to zero, indicating that all or someoneof X columns are significant
- The p-value for VOL and WT are higher 5% indicating some interaction issue among themselves, which need to be further explored


# In[61]:


performance metrics for model1


# In[63]:


# find the performance metrics
# create a data frame with actual y and predicted y columns
df1 = pd.DataFrame()
df1["actual_y1"] = cars["MPG"]
df1.head()


# In[65]:


# predict for the given X data columns
pred_y1 = model1.predict(cars.iloc[:,0:4])
df1["pred_y1"] = pred_y1
df1.head()


# In[67]:


# compute the mean squared error (MSE), RMS foe model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df1["actual_y1"], df1["pred_y1"])
print("MSE :", mse )
print("RMSE :",np.sqrt(mse))


# In[ ]:


# Compute VIF values
rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared
vif_hp = 1/(1-rsq_hp)

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars).fit().rsquared  
vif_wt = 1/(1-rsq_wt) 

rsq_vol = smf.ols('VOL~WT+SP+HP',data=cars).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars).fit().rsquared  
vif_sp = 1/(1-rsq_sp) 

# Storing vif values in a data frame
d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# In[ ]:


Obervations for VLF values:
- This ideal range of VIF values shall be b/w 0 to 10. However slightly higher values can be toleted
- As seen from the very high VIF values for VOL and WT, it is clear that they are prone to multicollinearity problem
- Hence it is decided to drop one of the columns (either Vol or WT) to overcome the multiollinearit
-it is decided to drop WT and retain VOL olumn in further models


# In[75]:


cars1 = cars.drop("WT", axis=1)
cars1.head()


# In[77]:


#Build model2 on cars1 dataset
import statsmodels.formula.api as smf
model2=smf.ols('MPG~HP+VOL+SP', data=cars).fit()
model2.summary()


# In[73]:


df2 = pd.DataFrame()
df2["actual_y2"] =cars["MPG"]
df2.head()


# In[79]:


pred_y2 = model2.predict(cars.iloc[:,0:4])
df2["actual_y2"] = pred_y2
df2.head()


# In[ ]:


Observations from model2 summary()
-The adjusted R-squared value improved slightly to 0.76
-All the p-values for model parameters are less than 5% hence they are significant
- therefore the HOP, VOL, SP columns are finalized as the significant predictor for the MPG response variable
- there is no improvement in MSE value


# In[ ]:


#### Leverage (Hat Values):
Leverage values diagnose if a data point has an extreme value in terms of the independent variables. A point with high leverage has a great ability to influence the regression line. The threshold for considering a point as having high leverage is typically set at 3(k+1)/n, where k is the number of predictors and n is the sample size.


# In[83]:


# Define variables and assign values
k = 3 # no of x-columns in cars1 
n= 81 # no of observation (rows)
leverage_cutoff = 3*((k + 1)/n)
leverage_cutoff


# In[85]:


from statsmodels.graphics.regressionplots import influence_plot

influence_plot(model2,alpha=.05)

y=[i for i in range(-2,8)]
x=[leverage_cutoff for i in range(10)]
plt.plot(x,y,'r+')

plt.show()


# In[ ]:


observations
-from the above plot, it is evident that data points 65,70,76,79,80 are the influencers.
- as their H Leverage values are higher and size is higher


# In[87]:


cars1[cars1.index.isin([65,70,76,79,80])]


# In[101]:


# Discrad the data points which are influence and reasign the row number (reset_independent)
cars2=cars.drop(cars1.index[[65,70, 76,78,79,80]],axis=0).reset_index(drop=True)


# In[103]:


# Rebuild the model model
model3= smf.ols('MPG~VOL+SP+HP',data = cars2).fit()
model3.summary()


# In[105]:


df3= pd.DataFrame()
df3["actual_y3"] =cars2["MPG"]
df3.head()


# In[109]:


# predict on all X data columns
pred_y3 = model3.predict(cars2.iloc[:,0:3])
df3["pred_y3"] = pred_y3
df3.head()


# In[115]:


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df3["actual_y3"], df3["pred_y3"])
print("MSE :", mse )
print("RMSE :",np.sqrt(mse))


# In[119]:


#### Comparison of models
                     

| Metric         | Model 1 | Model 2 | Model 3 |
|----------------|---------|---------|---------|
| R-squared      | 0.771   | 0.770   | 0.885   |
| Adj. R-squared | 0.758   | 0.761   | 0.880   |
| MSE            | 18.89   | 18.91   | 8.68    |
| RMSE           | 4.34    | 4.34    | 2.94    |


- **From the above comparison table it is observed that model3 is the best among all with superior performance metrics**


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




