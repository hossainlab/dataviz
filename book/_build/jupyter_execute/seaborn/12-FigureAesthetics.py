#!/usr/bin/env python
# coding: utf-8

# # Figure aesthetics: overriding and scaling plot elements

# Modify the features of the styles itself

# ## Overriding elements of Seaborn Styles

# Let us first check if we can figure out the basic features of the various Seaborn styles.

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


fb_data=pd.read_csv('datasets/dataset_Facebook.csv',
                     sep=r'\s*;\s*', engine='python')


# In[3]:


sns.axes_style()


# The above command dumps out the details of the currently enabled axes style.
# 
# The parameters that are part of the style definition can be overridden by passing a dictionary of parameters as below:

# In[4]:


f,ax=plt.subplots(figsize=(10,5))
sns.distplot(fb_data['Lifetime Post Total Reach'])


# Above is the plot with the basic style setting. Let us now try varying some parameters to see the effect on our plot.

# In[5]:


sns.set_style("ticks",{'xtick.major.size': 8,
                        'xtick.minor.size': 4.0,
                        'ytick.color': 'g',
                        'xtick.color': 'b',
                        'axes.facecolor': 'y',
                        'ytick.direction': 'in'})

f,ax=plt.subplots(figsize=(10,5))
sns.distplot(fb_data['Lifetime Post Total Reach'])


# We see that the complete control is in our hands. We can make the graph look however we think is suitable for our application.

# ## Scaling plot elements

# Most often, working on data analysis using plots will involve presenting the same to a wider audience through a presentation or poster.  Very often, we find that the simple graphs plotted here do not have the same impact on the bigger projector screen, or say a poster. 
# 
# To avoid this issue, Seaborn provides the flexibility to control the scale of plot elements, which means we can use the same code to simply create appropriatey sized plots.

# In[6]:


sns.set()


# There are four preset contexts available on Seaborn - a paper mode, a notebook mode, one for talks and one for posters. Lets take a look at these 4 options below. These can be set using the set_context label.

# In[7]:


sns.set_context("paper")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[8]:


sns.set_context("talk")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[9]:


sns.set_context("poster")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[10]:


sns.set_context("notebook")

f,ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[ ]:




