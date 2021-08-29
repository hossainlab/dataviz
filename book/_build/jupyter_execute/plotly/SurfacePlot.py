#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# ## Topographical 3D Surface Plot
# Given a the elevation for a set of x,y coordinates, we can draw a surface plot to represent the elevations in the landscape. This is useful to map out geological features given a set of elevations along with the latitudes and longitudes for instance.

# #### Define a matrix of z values 
# Assume these z values represent the elevations while the indices of the 2D list represent the x,y coordinates.

# In[2]:


z = [[16, 18, 17, 16],
     [15, 17, 17, 16],
     [12, 14, 12, 14]]


# #### Generate a surface plot
# We simply pass the list of z values while the x and y values are inferred (corresponding to the shape of the z list)

# In[3]:


data = [go.Surface(z = z)]


# #### Display the plot
# We see that all the points have been connected by 2D surfaces in order to generate the surface plot in 3-dimensional space.
# 
# One may need to zoom out to view the full plot

# In[4]:


offline.iplot(data)


# ### Real-life use case
# We obtain the elevations for a set of points for a volcano. The columns represent the x coordinates while the rows denote the y coordinates.

# In[5]:


volcano = pd.read_csv('https://python-graph-gallery.com/wp-content/uploads/volcano.csv')
volcano


# #### Generate a 2D numpy array containing our z values

# In[6]:


volcano.values


# #### Define the surface plot
# Here, we use volcano.values to produce a 2D numpy array which will be used to generate the plot. We can also specify the colorscale we would like to use for this representation.

# In[7]:


data = [go.Surface(z = volcano.values, 
                   colorscale = 'Jet')]


# In[8]:


layout = go.Layout(title='Volcano Elevation',
                   autosize=False,
                   width=500,
                   height=500
                  )


# In[9]:


fig = go.Figure(data=data, layout=layout)

offline.iplot(fig)


# In[ ]:




