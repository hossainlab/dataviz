#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Produce a trace

# In[2]:


trace0 = go.Scatter(x = [10, 20, 30],
                    y = [40, 30, 20]
)


# #### The second trace references xaxis2 and yaxis2 in the layout
# This is set by assigning th values of x2 and y2 to the xaxis and yaxis fields.

# In[3]:


trace1 = go.Scatter(x = [2, 3, 4],
                    y = [3, 4, 5],
                    
                    xaxis = 'x2',
                    yaxis = 'y2'
)


# In[4]:


data = [trace0, trace1]


# #### Define the layout
# The domain field sets the position of the axis in the plot. The list contains 2 values representing the left and right extents (for X axis) along with the top bottom and top extents (for Y axis). The extents are specified on a 0-1 scale where 0 is the left or bottom while 1 is the right or top of the plot.
# 
# For instance, the inset X axis will begin from 60% of the plot width to 90%. The inset Y axis from 50% of the height to 80%. 

# In[5]:


layout = go.Layout(xaxis2 = dict(domain = [0.6, 0.9],
                                 anchor='y2'
                                ),
                   
                   yaxis2 = dict(domain = [0.5, 0.8],
                                 anchor='x2'
                                )
)


# In[6]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# ### Planet data set
# 
# We use the planets dataset once again. This data has been compiled from publicly available sources. 

# In[7]:


data= pd.read_csv('datasets/planets.csv')
data.head()


# #### Generate one bar graph showing the distance of each planet from the Sun

# In[8]:


trace0 = go.Bar(x = data['planet'],
                y = data['distance_from_sun'],
                
                name = 'Distance From the Sun (million km)'
               )


# #### The second trace shows the period of revolution in Earth Days
# This is mapped to xaxis2 and yaxis2 in the layout

# In[9]:


trace1 = go.Bar(x=data['planet'],
                y=data['period_of_revolution_around_sun'],
              
                xaxis='x2',
                yaxis='y2',
              
                name='Revolution Period (Earth Days)'
               )


# In[10]:


data = [trace0, trace1]


# #### Define inset axes positions in the layout
# The inset X axis begins from 20% of the plot width to 50%. The Y axis from 60% to 90% of the plot height.

# In[11]:


layout = go.Layout(xaxis2 = dict(domain = [0.2, 0.5],
                                 anchor ='y2'),
                   
                   yaxis2 = dict(domain = [0.6, 0.9],
                                 anchor = 'x2'
                                )
                  )


# #### Plot the figure
# The placement of the plots should ensure that it does not overlap with another plot and obscure it - as we have done here.

# In[ ]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# ### Subplots
# Given our flexibility in placing the axes of a plot, we can even generate multiple graphs in a figure if we're careful about how we position the individual plots

# #### Define the layout to produce 

# In[21]:


layout = go.Layout(xaxis = dict(domain = [0.0, 0.45]),
                   
                   xaxis2 = dict(domain = [0.55, 1.0]),
                   
                   yaxis2 = dict(overlaying='y',
                                 anchor = 'free',
                                 position = 0.55
                                )

                  )


# In[22]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# In[ ]:




