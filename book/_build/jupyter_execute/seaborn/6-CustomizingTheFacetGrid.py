#!/usr/bin/env python
# coding: utf-8

# ## Customising the FacetGrid plots
# Let us now try to use other features offered by FacetGrid to make our plots even better.

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


fb_data=pd.read_csv('datasets/dataset_Facebook.csv',
                     sep=r'\s*;\s*', engine='python')


# In[ ]:





# **Defining the bars**
# * We have specified bar chart colour and edge colour and line width

# In[3]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=4)

g.map(sns.barplot,"Post Weekday","Page total likes", color="#334488", edgecolor="red", lw=.5)


# **To adjust spacing between plots**

# In[17]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=3)
g.map(sns.barplot,"Post Weekday", "Page total likes",color="#aaff33", edgecolor="white", lw=.5)

g.fig.subplots_adjust(wspace=1, hspace=0.5);


# **Setting axes labels**

# In[22]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=4)

g.map(sns.barplot,"Post Weekday","Page total likes",color="#eedff0", edgecolor="white", lw=.5)

g.set_axis_labels("Posts every week", "Total likes");


# **Customising the axes points**

# In[9]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=3)

g.map(sns.barplot,"Post Weekday", "Page total likes", color="#13f0ff", edgecolor="white", lw=.5)
g.set_axis_labels("Posts every week", "Total likes");

g.set(yticks=[40000, 80000, 120000]);


# **Setting axes limits**

# In[24]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=3)

g.map(sns.barplot,"Post Weekday", "Page total likes", color="#2293aa", edgecolor="white", lw=.5)
g.set_axis_labels("Posts every week", "Total likes");
g.set(yticks=[40000, 80000, 120000]);

g.set(xlim=(0, 6), ylim=(0, 80000));


# *We see that setting y limit has cut off y axis at that limit. As x limit starts from zero, the centre of he first bar at indication 1 is taken as the zeroth limit; similarly with upper limit 6*
