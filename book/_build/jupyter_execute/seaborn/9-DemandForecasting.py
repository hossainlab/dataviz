#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# We have seen from the flowchart about the Seaborn approach to Machine Learning Problems. Let's try to practically see how this turns out.
# 
# Below, we have a dataset that describes the daily demand forecasting orders of a Brazilian logistics company. The data describes the demand over a period of 60 days. 
# 
# Let us look at the particulars, see what we want to observe and take the help of Seaborn to see what Machine Learning approach we will have to use to analyse further data.

# In[3]:


order_data=pd.read_csv('datasets/Daily_Demand_Forecasting_Orders.csv',
                       names=["index","Day of the week","Non-urgent order","urgent order", 
                              "Type A","Type B", "Type C" , "Fiscal sector orders","Traffic controller orders",
                              "Banking orders (1)","Banking orders (2)","Banking orders (3)", "Target"],
                       skiprows=1,
                       sep=r'\s*;\s*', engine='python')


# Let us now plot a few basic plots to see what our data holds.

# In[126]:


#Plotting a jointplot to see relationship between Banking orders(2) and Type A orders
sns.jointplot(y='Type A', x='Banking orders (2)', data=order_data)


# The resulting scatter plot has data randomly spread out. Banking orders(2) has a reasonable type A category across a wide range of order quantities. There might be some pattern, but we will have to go through some more months of data to figure that out. Let's call it plot 1.

# In[4]:


sns.jointplot(y='urgent order', x='Target', data=order_data)


# The scatter plot above is also random, but looking at the way the points are placed, there seems to be a linear relationship of some kind between the variables in the graph. As the target number of orders increases, so does the number of urgent orders. Call it plot 2.

# In[5]:


sns.jointplot(y='Target', x='Day of the week', data=order_data)


# Above, we have plot 3 that plots the target orders versus the days of the week. Just seeing the plot, we can see that it is divided into certain categories. As we know that the categories are the days of the week, the order is basically classified into the five working days of the week.

# In[10]:


corrmat = order_data.corr()
f, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corrmat, vmax=.8, square=True, annot=True, fmt='.2f', cmap = "winter")
plt.show()


# In[ ]:




