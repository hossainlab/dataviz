#!/usr/bin/env python
# coding: utf-8

# # Seaborn themes and figure styles

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


fb_data=pd.read_csv('datasets/Facebook_metrics/dataset_Facebook.csv',
                     sep=r'\s*;\s*', engine='python')


# In[4]:


fb_data.head()


# In[5]:


f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# 
# 

# In[6]:


sns.set()


# In[7]:


f,ax=plt.subplots(figsize=(10,5))
sns.distplot(fb_data['Lifetime Post Total Reach'])


# *As soon as we set the plot to its default and plotted the graph again, we notice the change in pattern. Shows that our notebook was not in the default mode earlier*

# Seaborn has five preset themes - darkgrid, whitegrid, dark, white and ticks. Let us see each of these one by one.

# Whitegrid - white background, with grids on the plot

# In[8]:


sns.set_style("whitegrid")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# White grid on a dark background. This is the default mode.

# In[9]:


sns.set_style("darkgrid")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# Plain dark background

# In[10]:


sns.set_style("dark")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# Plain white background

# In[11]:


sns.set_style("white")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# Add ticks along the axes for each unit

# In[12]:


sns.set_style("ticks")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# ** For all the above settings, the graph style is set for all plots that follow. What if we want to use a different style for just a single plot, and then fall back to the original style?**

# In[13]:


with sns.axes_style("darkgrid"):
    
    f,ax=plt.subplots(figsize=(10,5))

    sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[15]:


f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])

sns.despine()


# Following from what we said above, as the last axes style was set to ticks, we see that the above plot has retained the ticks style, but we see that there is no box surrounding the plot. The right and top lines have been despined.

# In[16]:


f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])

sns.despine(left=True, right=False, bottom=True, top=False)


# There is an additional 'trim' parameter that can be used while making our plots. This is what Seaborn has to say about the feature:
# "Some plots benefit from offsetting the spines away from the data, which can also be done when calling despine(). When the ticks don’t cover the whole range of the axis, the trim parameter will limit the range of the surviving spines."

# In[17]:


f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])

sns.despine(offset=15, trim=True)


# In[ ]:




