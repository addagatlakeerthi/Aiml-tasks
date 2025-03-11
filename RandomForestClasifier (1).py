#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Random forest classifier uses training data to create mutliple data rates using "Boot Strapping" method random seletion with replacement


# In[1]:


import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import  DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold


# In[2]:


dataframe = pd.read_csv("diabetes.csv")
dataframe


# In[3]:


#### **Overview of Pima Indian diabetes dataset**

-Preg	Number of times pregnant	Numeric	[0, 17]

-Gluc	Plasma glucose concentration at 2 Hours in an oral glucose tolerance test (GTIT)	Numeric	[0, 199]

-BP	Diastolic Blood Pressure (mm Hg)	Numeric	[0, 122]

-Skin	Triceps skin fold thickness (mm)	Numeric	[0, 99]

-Insulin	2-Hour Serum insulin (µh/ml)	Numeric	[0, 846]

-BMI	Body mass index [weight in kg/(Hehight in m)]	Numeric	[0, 67.1]

-DPF	Diabetes pedigree function	Numeric	[0.078, 2.42]

-Age	Age (years)	Numeric	[21, 81]

-Outcome	Binary value indicating non-diabetic /diabetic	Factor	[0,1]


# In[6]:


from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import  RandomForestClassifier

X = dataframe.iloc[:,0:8]
Y = dataframe.iloc[:,8]

kfold = StratifiedKFold(n_splits=10, random_state= 3,shuffle=True)

model = RandomForestClassifier(n_estimators= 200,random_state= 20,max_depth=None)
results = cross_val_score(model, X, Y, cv=kfold)
print(results)
print(results.mean())


# In[ ]:


number of trees (n_estimates): number of trees in the forest
but also increse the computational cost and time
max depth of trees : cotrols the max depth of each tree
depth is a commom method to prevent overfitting
min samples split : determines the mim number of the model forom keaning overly specific patterns thus reduci g overfitting
min samples split: mim  number of 


# In[10]:


from sklearn.model_selection import GridSearchCV
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
params = {
    'max_depth':[2,3,5,None],
    'min_samples_leaf':[5,10,20],
    'n_estimators':[50,100,200,500],
    'max_features':["squt","log2",None],
    'criterion':["gini","entropy"]
}
grid_search = GridSearchCV(estimator=rf,
                           param_grid=params,
                           cv = 5,
                           n_jobs=-1, verbose=10, scoring="accuracy")
grid_search.fit(X, Y)


# In[12]:


print(grid_search.best_params_)
print(grid_search.best_score_)


# In[14]:


grid_search.best_estimator_


# In[20]:


model_best = RandomForestClassifier(criterion='entropy', max_depth=5, max_features=None,
                                   min_samples_leaf=5, n_jobs=-1, random_state=42)
model_best.fit(X,Y)
model_best.feature_importances_


# In[26]:


X = dataframe.iloc[:,0:8]
X.columns


# In[38]:


df = pd.DataFrame(model_best.feature_importances_, columns = ["Importance score"],index = X.columns)
df.sort_values(by = "Importance score", inplace = True, ascending = False,) 


# In[36]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.bar(df.index, df["Importance score"])


# In[ ]:




