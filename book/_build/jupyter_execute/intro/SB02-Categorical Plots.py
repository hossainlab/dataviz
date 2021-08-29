#!/usr/bin/env python
# coding: utf-8

# # Categorical Data Plots

# In[2]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')
tips.head()


# ## Barplot and Countplot
# 
# These very similar plots allow you to get aggregate data off a categorical feature in your data. **barplot** is a general plot that allows you to aggregate the categorical data based off some function, by default the mean.

# ### Barplot 

# In[4]:


sns.barplot(x='sex',y='total_bill',data=tips)


# __Note__
# 
# You can change the estimator object to your own function, that converts a vector to a scalar:

# In[6]:


# import numpy
import numpy as np


# In[7]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# ### Countplot
# 
# This is essentially the same as barplot except the estimator is explicitly counting the number of occurrences. Which is why we only pass the x value

# In[8]:


sns.countplot(x='sex',data=tips)


# ## Boxplot and Violinplot
# 
# `boxplots` and `violinplots` are used to shown the distribution of categorical data. A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

# ### Boxplot

# In[9]:


sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[10]:


# Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')


# In[11]:


sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")


# ### Violinplot
# A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.

# In[27]:


sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[12]:


sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')


# In[13]:


sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')


# ## Stripplot and Swarmplot
# The stripplot will draw a scatterplot where one variable is categorical. A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.
# 
# The swarmplot is similar to stripplot(), but the points are adjusted (only along the categorical axis) so that they don’t overlap. This gives a better representation of the distribution of values, although it does not scale as well to large numbers of observations (both in terms of the ability to show all the points and in terms of the computation needed to arrange them).

# In[14]:


sns.stripplot(x="day", y="total_bill", data=tips)


# In[15]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)


# In[16]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')


# In[24]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)


# In[18]:


sns.swarmplot(x="day", y="total_bill", data=tips)


# In[23]:


sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)


# ## Combining Categorical Plots

# In[20]:


sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)


# ## Factorplot
# 
# factorplot is the most general form of a categorical plot. It can take in a **kind** parameter to adjust the plot type

# In[22]:


sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')

