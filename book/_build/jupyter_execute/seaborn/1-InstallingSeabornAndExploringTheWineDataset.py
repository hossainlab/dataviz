#!/usr/bin/env python
# coding: utf-8

# # Visualizing Relationships and Distributions in Seaborn

# ### Getting into the seaborn domain

# In[2]:


get_ipython().system('pip3 install seaborn')


# In[4]:


import seaborn as sns


# In[13]:


print(sns.__version__)


# ### What data do we work on
# Ideally, data in a tabulated format - dataframe
# 
# #### We use the Pandas library for generating dataframes

# In[5]:


import pandas as pd


# In[14]:


print(pd.__version__)


# * Load dataset into pandas from a .csv file; store it as a dataframe
# * File downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
# * Even though the file comes with headers, we still specify them so that they are in our desired format

# In[7]:


wine_data = pd.read_csv('datasets/winequality-white.csv', 
                        names=["Fixed Acidity", "Volatile Acidity", "Citric Acid", "Residual Sugar",
                                "Chlorides", "Free Sulfur Dioxide", "Total Sulfur Dioxide", "Density", 
                                "pH", "Sulphates", "Alcohol", "Quality"],
                        skiprows=1,
                        sep=r'\s*;\s*', engine='python')


# In[8]:


wine_data.head()


# In[9]:


#Displaying the bottom 5 entries
wine_data.tail()


# *The dataset discusses different wine samples and their qualities*
# The dataset has details about the content of alcohol, sugar, different acids in each wine sample and even has a wine quality represented by numbers.

# In[12]:


print(len(wine_data.index))


# In[11]:


wine_data.describe()


# In[ ]:




