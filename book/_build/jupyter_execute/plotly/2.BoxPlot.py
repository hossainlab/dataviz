#!/usr/bin/env python
# coding: utf-8

# create traces

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Download the Automobile dataset
# Dataset location: https://www.kaggle.com/toramky/automobile-dataset

# In[2]:


import pandas as pd

auto_data = pd.read_csv('datasets/Automobile_data.csv')
auto_data.head()


# #### Examine the two fields we will use in our plots
# View the distribution of values for these columns. The box plot will help us visualize this data

# In[3]:


auto_data[['city-mpg', 'highway-mpg']].describe()


# #### The first boxplot will model the City MPG

# In[4]:


trace0 = go.Box(y = auto_data['city-mpg'], 
                name = 'City MPG')


# #### The second boxplot will model the Highway MPG

# In[5]:


trace1 = go.Box(y = auto_data['highway-mpg'], 
                name = 'Highway MPG')


# #### Plot the data 

# In[6]:


data = [trace0, trace1]

offline.iplot(data)


# # Styling Outliers

# #### Define the first boxplot
# The value of <b>boxpoints</b> decides which points are plotted separtely with markers rather than being represented by a box. The default value is 'outliers'. A value of 'all' will plot all the points outside the box (in addition to plotting the box).
# 
# Other possible values for boxpoints are 'suspectedoutliers' (values outside a certain range) and False (where only a box is drawn)
# 
# <b>boxmean</b> defines whether a dotted line will be drawn to represent the mean of the distribution

# In[7]:


trace0 = go.Box(y = auto_data['city-mpg'], 
                name = 'City MPG', 
                
                boxpoints = 'all',
                
                boxmean = True                
               )


# #### Define the second boxplot
# A value of 'sd' for <b>boxmean</b> will also show the standard deviation for the distribution along with the mean

# In[8]:


trace1 = go.Box(y = auto_data['highway-mpg'], 
                name = 'Highway MPG', 
                
                boxmean = 'sd'
               )


# In[9]:


data = [trace0, trace1]

offline.iplot(data)


# ### More styling

# #### Style the first boxplot
# * <b>marker</b> defines the markers (by default only the outliers)
# * <b>line</b> configures the enclosing box lines and the whiskers. The default width is 2

# In[10]:


trace0 = go.Box(y = auto_data['city-mpg'], 
                name = 'City MPG',
                
                marker = dict(color = 'skyblue'),
                
                line = dict(color = 'navy', 
                            width = 1)  
               )


# #### Style the second boxplot
# * <b>fillcolor</b> sets the color with which to fill the box. The default is the line color with 50% transparency
# * <b>symbol</b> for the marker has a number of options (https://plot.ly/python/reference/#box-marker-symbol)

# In[15]:


trace1 = go.Box(y = auto_data['highway-mpg'], 
                name = 'Highway MPG',
                
                fillcolor = 'bisque',
                
                marker = dict(color = 'deeppink', 
                              symbol = 'square'),
                
                line = dict(color = 'tomato')
               )


# In[16]:


data = [trace0, trace1]

offline.iplot(data)


# In[ ]:





# In[ ]:





# In[ ]:




