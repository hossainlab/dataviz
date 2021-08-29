#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### We produce 5 sets of values
# A 3D bubble chart can be used to represent multiple dimensions of data. Aside from the 3 spatial dimensions, markers can represent more information from their size and color giving a total of 5 features which can be represented

# In[2]:


n = 50

random_x = np.random.randn(n)

random_y = np.random.randn(n)

random_z = np.random.randn(n)

random_a = np.random.randn(n)

random_b = np.random.randn(n)


# #### Generate a 3D scatter trace using the 5 dimensions 
# We use a color scale to pick the bubble colors. The random_b list needs to be multiplied by 1000 to appear clearly in the plot

# In[3]:


trace = go.Scatter3d(x = random_x,
                     y = random_y,
                     z = random_z,
                   
                     mode = 'markers',
                     
                     marker = dict(color = random_a,
                                   colorscale = 'Rainbow',
                                          
                                   sizemode = 'area',
                                   size = 1000*random_b
                                   )
                    )
data=[trace]


# In[4]:


offline.iplot(data)


# ### 3D Bubble chart to plot real data
# This is the same dataset we had used for the 2D bubble chart. This data has been compiled using publicly available information

# In[5]:


planets= pd.read_csv('./datasets/planets.csv')
planets


# #### Define colors to represent each planet
# This list of colors represents the primary color of the respective planets. Source is: https://colorhunt.co/blog/solar-system-stars-color-palettes/
# 
# We will be conveying the color of the planet using this color list

# In[6]:


colors = ['#D5D2D1', 
          '#F8B581', 
          '#182A61', 
          '#B53B03', 
          '#B9CBD5', 
          '#E0CDAD', 
          '#D3F9FA',
          '#3454DF', 
          '#E9E8D2']


# #### Define the 3D scatter plot
# We convey the following information in the plot:
# * <b>x-axis</b> represents the distance from the Sun
# * <b>y-axis</b> denotes the time taken (in Earth days) for the planet to revolve around the Sun
# * <b>z-axis</b> conveys the number of moons for the planet
# * <b>marker size</b> portrays the size of the planet (diameter)
# * <b>marker colors</b> represent the color of the planet

# In[7]:


trace = go.Scatter3d(x = planets['distance_from_sun'],
                     y = planets['period_of_revolution_around_sun'],
                     z = planets['no_of_moons'],
                     
                     text=planets['planet'],
                     
                     mode='markers',
                     marker=dict(sizemode='diameter',
                                 sizeref=750,
                                 size=planets['planet_diameter'],
                                 color = colors
                                 )
                    )
data=[trace]


# #### Define the layout
# Aside from the figure dimensions, we specify the appearance of the axes. Since we have picked a dark background color, we will use light colors for the axes lines and text.

# In[8]:


layout = go.Layout(width=800, 
                   height=800, 
                   title = 'Planets of our Solar System',
                   
                   scene = dict(xaxis=dict(title='Distance from Sun',
                                           color='white',
                                           titlefont=dict(color='yellow')
                                          ),
                                
                                yaxis=dict(title='Revolution Period (Earth days)',
                                           color='white',
                                           titlefont=dict(color='yellow')
                                          ),
                                
                                zaxis=dict(title='Moon Count',
                                           color='white',
                                           titlefont=dict(color='yellow')),
                                
                                bgcolor = '#141836'
                               )
                  )


# #### Plot the figure
# The large planets are quite prominent, and we need to zoom in to view the smaller ones.

# In[9]:


fig=go.Figure(data=data, 
              layout=layout)

offline.iplot(fig)


# In[ ]:





# In[ ]:




