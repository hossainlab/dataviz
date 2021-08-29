#!/usr/bin/env python
# coding: utf-8

# In[25]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Plot a simple heatmap
# The required argument for a Heatmap is <b>z</b> - a 2D list containing the set of values which need to be portrayed using a colorscale. THe heatmap is a 2D grid in the same shape as z with different colors denoting the values of the elements of z. 
# 
# The simplest heatmap is a single 1-dimensional list

# In[36]:


trace = go.Heatmap(z = [[2, 40, 60]])


# #### By default, the color scale is displayed

# In[37]:


data=[trace]

offline.iplot(data)


# #### The more common case is to use a proper 2D list

# In[46]:


trace = go.Heatmap(z = [[2, 40, 60], 
                       [31, 3, 18], 
                       [24, 13, 54]])


# #### The first list is at the bottom of the heatmap

# In[47]:


data=[trace]

offline.iplot(data)


# ### A more practical example
# One can plot a heatmap using categorical data for the X and Y axes. The values in these axes must be unique. This will plot a grid if the shape (x,y) and z must conform to that shape
# 
# Consider there are three cartons with 5 different varieties of fruits. And z is number of the respective fruit in the carton

# In[ ]:


x=['Mango', 'Strawberry', 'Mulberry', 'Orange', 'Watermelon']

y=['Carton 1', 'Carton 2', 'Carton 3']


# #### Plot the heatmap
# We specify a colorscale to use. We specify the reversecale attibute which reverses the colors used in the colorscale. For example, with our reversescale, the lower z values are represented by yellow and the higher values are dark blue. Without the reversescale, this would have been reversed. 

# In[73]:


trace = go.Heatmap(z = [[10, 20, 30, 40, 10], 
                       [20, 10, 50, 80, 30], 
                       [30, 50, 60, 10,  0]],
                   
                   x = x,
                   y = y,
                   
                   colorscale = 'Viridis',
                   reversescale = True
                  )


# In[74]:


data=[trace]

offline.iplot(data)


# In[ ]:




