#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### A regular 2D scatter plot

# In[2]:


x = [1, 2, 3, 4]
y = [2, 4, 1, 5]

trace = go.Scatter(x=x,
                   y=y,
                   mode='markers',
                  )

data = [trace]

offline.iplot(data)


# #### We introduce a 3rd dimension

# In[3]:


z = [70, 40, 30, 20]


# #### This 3rd dimension can be portrayed by the marker size
# The marker size is in pixels. The default is 6.

# In[4]:


trace = go.Scatter(x=x,
                   y=y,
                   mode='markers',
                   
                   marker = dict(size = z)
)


# #### Plot the Bubble chart
# By using the size of the bubble, we can convey one more set of features

# In[5]:


data = [trace]

offline.iplot(data)


# #### We define a 4th set of features

# In[6]:


a = [11, 35, 99, 56]


# #### The 4th feature can be conveyed with a color scale

# In[7]:


trace = go.Scatter(x=x,
                   y=y,
                   mode='markers',
                   
                   marker = dict(size = z, 
                                 
                                 color = a,
                                 colorscale = 'Rainbow',
                                 showscale = True
                                )
)


# #### Plot the figure
# With bubbles, it is possible for us to convey 2 additional features using to the bubble size and color

# In[8]:


data = [trace]

offline.iplot(data)


# ## Portraying data about planets
# We can convey multiple points of information about our solar system's planets using a bubble chart.
# 
# The data has been compiled.

# In[9]:


data = pd.read_csv('./datasets/planets.csv')


# In[10]:


data


# #### Define the Bubble Chart
# 
# * planets are on the X axis
# * the Y axis denotes the distance from the sun (in KM)
# * the marker size represents the planet diameter
# * the color represents the number of moons
# 
# We can also set the hover text.
# 
# The sizeref attribute used sets the scale factor for the marker size. Setting it to 1000 has the same effect as dividing the size values (planet diameter in our case) by 1000.

# In[12]:


trace = go.Scatter(x = data['planet'],
                   
                   y = data['distance_from_sun'],
                   
                   mode = 'markers',
                   
                   marker =dict(size = data['planet_diameter'],
                                sizeref = 1000,

                                color = data['no_of_moons'],
                                colorscale = 'Rainbow',
                                showscale = True
                              ), 
                   
                   text =  [str(dia) + ' km' for dia in data['planet_diameter']]
    )
   


# In[13]:


data = [trace]


# #### Define the layout
# We set the figure dimensions and title. The hovermode of 'closest' will display the x,y and hovertext of the marker we are hovering over.

# In[14]:


layout = go.Layout(height = 600, 
                   width = 900,
                   
                   title = 'Planets of our Solar System',
                   
                   hovermode = 'closest')


# In[15]:


fig = go.Figure(data = data, 
                layout = layout)

offline.iplot(fig)


# In[ ]:





# In[ ]:




