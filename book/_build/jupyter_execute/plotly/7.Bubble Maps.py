#!/usr/bin/env python
# coding: utf-8

# In[18]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import math
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# starting with plotting a bubble on the newyork city and 0,0 lonititude latitude to understand how scatter geo works
# 
# 
# with default land color

# In[19]:


trace = dict (type='scattergeo',
              
              lon = [0,-74] ,
              lat = [0,40.7],
              
              marker = dict (size=10),
              
              mode='markers',
    
) 

data=[trace]


# In[20]:


layout = dict(showlegend = False,
              
              geo = dict(showland = True)
             )


# In[21]:


fig=dict(data=data,
         layout=layout)


# In[22]:


offline.iplot(fig)


# ### Download the Meteorite Landings dataset
# Dataset location: https://www.kaggle.com/nasa/meteorite-landings
# 
# This contains a list of over 45,000 meteorite landings from the year 301 until 2013. Includes a handful of predicted landings in the future.

# In[41]:


data = pd.read_csv('datasets/meteorite-landings.csv')
data.tail()


# #### We restrict our data to meteors which landed in the year 2007
# We don't wish to plot 45,000 meteor landings on our map

# In[42]:


df_2007 = data[data['year'] == 2007]


# #### Obtain the list of latitudes and longitudes
# These will make up the x and y coordinates of our plot. We have to round up longitudes and latitudes as the points plotted by original values are not accurate

# In[44]:


latitudes = df_2007['reclat'].round(2)
longitudes = df_2007['reclong'].round(2)


# #### We set a scaling factor
# Since the bubbles on our plot will represent the mass of the meteors, they will be rather large by default. For that reason we apply a scaling factor for the marker size

# In[12]:


scale=100


# #### Define the trace
# We set the following attributes:
# * latitudes and longitudes of the meteor landing sites
# * the hovertext will contain the name of the meteor
# * the area of the markers will represent the mass of the meteor with a scaling factor 

# In[62]:


trace = dict (type='scattergeo',
              
              lat = latitudes,
              lon = longitudes ,
              
              text = df_2007['name'],
              
              marker = dict (size=df_2007['mass']/scale,
                             sizemode = 'area'),
              
              mode='markers',
    
) 

data=[trace]


# #### Define the layout
# Here, we set the color to use to represent the landmass

# In[63]:


layout = dict(title = '2007 Meteorite Landings',
              showlegend = False,
              
              geo = dict(showland = True,
                         landcolor = '#ccff33'
                        )
             )


# In[64]:


fig=dict(data=data,
         layout=layout)


# In[65]:


offline.iplot(fig)


# In[ ]:




