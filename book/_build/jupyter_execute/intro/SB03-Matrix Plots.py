#!/usr/bin/env python
# coding: utf-8

# # Matrix Plots
# 
# Matrix plots allow you to plot data as color-encoded matrices and can also be used to indicate clusters within the data (later in the machine learning section we will learn how to formally cluster data).
# 
# Let's begin by exploring seaborn's heatmap and clutermap:

# In[3]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


flights = sns.load_dataset('flights')


# In[5]:


tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[7]:


flights.head()


# ## Heatmap
# 
# In order for a heatmap to work properly, your data should already be in a matrix form, the sns.heatmap function basically just colors it in for you. For example:

# In[8]:


tips.head()


# In[9]:


# Matrix form for correlation data
tips.corr()


# In[10]:


sns.heatmap(tips.corr())


# In[11]:


sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)


# Or for the flights data:

# In[12]:


flights.pivot_table(values='passengers',index='month',columns='year')


# In[13]:


pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)


# In[14]:


sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)


# ## Clustermap
# 
# The clustermap uses hierarchal clustering to produce a clustered version of the heatmap. For example:

# In[15]:


sns.clustermap(pvflights)


# Notice now how the years and months are no longer in order, instead they are grouped by similarity in value (passenger count). That means we can begin to infer things from this plot, such as August and July being similar (makes sense, since they are both summer travel months)

# In[16]:


# More options to get the information a little clearer like normalization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

