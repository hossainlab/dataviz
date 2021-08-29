#!/usr/bin/env python
# coding: utf-8

# # Style and Color
# 
# We've shown a few times how to control figure aesthetics in seaborn, but let's now go over it formally:

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')


# ## Styles
# 
# You can set particular styles

# In[3]:


sns.countplot(x='sex',data=tips)


# In[4]:


sns.set_style('white')
sns.countplot(x='sex',data=tips)


# In[5]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')


# ## Spine Removal

# In[6]:


sns.countplot(x='sex',data=tips)
sns.despine()


# In[7]:


sns.countplot(x='sex',data=tips)
sns.despine(left=True)


# ## Size and Aspect

# You can use matplotlib's **plt.figure(figsize=(width,height) ** to change the size of most seaborn plots.
# 
# You can control the size and aspect ratio of most seaborn grid plots by passing in parameters: size, and aspect. For example:

# In[8]:


# Non Grid Plot
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)


# In[10]:


# Grid Type Plot
sns.lmplot(x='total_bill',y='tip',height=2,aspect=4,data=tips)


# ## Scale and Context
# 
# The set_context() allows you to override default parameters:

# In[11]:


sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')

