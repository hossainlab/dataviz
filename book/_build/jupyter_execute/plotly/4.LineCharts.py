#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# ## Style Line Plots
# We have seen how line plots can be plotted. Now we see how those can be formatted

# ### Download data set
# Europe international tourist arrivals by region over time.
# 
# Dataset location: https://www.e-unwto.org/doi/pdf/10.18111/9789284419029

# In[2]:


import pandas as pd

tourism_data = pd.read_csv('datasets/europe_tourism.csv')
tourism_data


# #### The first trace
# Plot a line for Western Europe's tourism numbers. We format the line by:
# * specifying a color in RGB format (we can also use RGBA)
# * specify a width

# In[3]:


trace0 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Western'],
    
    name = 'Western Europe',
    
    line = dict(color = ('rgb(0, 250, 24)'),
                width = 4)
)


# #### The second trace
# Plot the line for Eastern Europe's tourism numbers. We format the line by:
# * specifying a color in RGB format
# * specify a width
# * use a dotted line using the 'dash' attribute

# In[4]:


trace1 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Eastern'],
    
    name = 'Eastern Europe',
    
    line = dict(color = ('rgb(205, 12, 24)'),
                width = 4,
                dash='dot')
)


# #### The last trace
# Plot a line for Southern Europe's tourism numbers. We format the line by:
# * specifying a color in RGBA format, with an alpha of 191/255
# * specify a width
# * this will be a dashed line

# In[5]:


trace2 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Southern'],
    
    name = 'Southern Europe',
    
    line = dict(color = ('rgba(2, 12, 240, 191)'),
                width = 4,
                dash = 'dash')
)


# #### Define the data and layout

# In[6]:


data = [trace0, trace1, trace2]

layout = dict(title = 'International Tourist Arrivals (millions)',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Tourists'),
              )


# #### Define and plot the figure

# In[7]:


fig = dict(data=data, layout=layout)

offline.iplot(fig)


# ## Connect Data Gaps
# Plotly can handle cases where the series to be plotted has missing data. It does so by connecting the points on either side of the missing data points.
# 
# To see this in action, we introduce missing data into our data set. Assume the tourism numbers for the year 2000 are unavailable for some reason.

# In[8]:


tourism_data['Western'].iat[2] = None
tourism_data['Eastern'].iat[2] = None
tourism_data['Southern'].iat[2] = None

tourism_data


# #### For the first trace, we fill in the gap
# By setting the connectgaps attribute to True, the line will remain continuous

# In[9]:


trace0 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Western'],
    
    name = 'Western Europe',
    
    line = dict(color = ('rgb(0, 250, 24)'),
                width = 4),
    
    connectgaps = True
)


# #### For the second trace, we don't fill the gap
# We explicitly set connectgaps to False. This will result in a gap in the line

# In[10]:


trace1 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Eastern'],
    
    name = 'Eastern Europe',
    
    line = dict(color = ('rgb(205, 12, 24)'),
                width = 4,
                dash='dot'),
    
    connectgaps = False
)


# #### For the third trace, we don't specify the value explicitly
# The default value of connectgaps is False, so the line is disconnected

# In[11]:


trace2 = go.Scatter(
    
    x = tourism_data['Year'],
    y = tourism_data['Southern'],
    
    name = 'Southern Europe',
    
    line = dict(color = ('rgba(2, 12, 240, 191)'),
                width = 4,
                dash = 'dash')
)


# In[12]:


data = [trace0, trace1, trace2]

layout = dict(title = 'International Tourist Arrivals (millions)',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Tourists'),
              )


# In[13]:


fig = dict(data=data, layout=layout)

offline.iplot(fig)


# ### Plots with Annotations 
# Plotly allows different forms of annotations to be added to a plot. We create a list of annotations which is later added to the layout

# In[14]:


annotations = []


# #### Annotation without an arrow
# The attributes for an annotation include:
# * The x and y coordinates where the annotation will appear
# * the x and y anchor values which determine which part of the annotation will be anchored to the (x,y) coordinates
# * The annotation text
# * The font of the annotation text
# * showarrow determines whether an arrow is used to point to (x,y)
# 
# This annotation marks the international tourist number for Western Europe at the beginning of our series - 1990.

# In[15]:


annotations.append(dict(x = tourism_data['Year'][0], 
                        y = tourism_data['Western'][0],
                            
                        xanchor='right', 
                        yanchor='middle',
                            
                        text = str(tourism_data['Western'][0]) + 'M',
                            
                        font=dict(family = 'Arial',
                                  size = 16,
                                  color = 'grey'
                                 ),
                                  
                        showarrow = False
                       )
                  )


# #### The second annotation has an arrow
# An arrow will be drawn from the xanchor,yanchor of the annotation text to the (x,y) point. We also have an arrowcolor.

# In[16]:


annotations.append(dict(x = tourism_data['Year'][5], 
                        y = tourism_data['Eastern'][5],
                            
                        xanchor='left', 
                        yanchor='bottom',
                            
                        text = str(tourism_data['Eastern'][5]) + 'M',
                            
                        font=dict(family = 'Arial',
                                  size = 16,
                                  color = 'grey'),
                                  
                        showarrow = True,
                        arrowcolor = 'grey'
                       )
                  )


# #### The third annotation uses the yref attribute
# By default, when we specify x and y values for the annotation, it is used to mark the (x,y) points using the units of the axis (#tourists vs year in our graph). When xref or yref is set to 'paper', the corresponding x or y coordinate is scaled to a value between 0 and 1.
# 
# Here, we want the annotation to appear 80% of the way up in the plot.
# 
# Each annotation also appears in a text box which is actually transparent. Here, we set a background color for the text box. 

# In[17]:


annotations.append(dict(yref='paper', 
                        
                        x = 2000, 
                        y = 0.8,
                        
                        text = 'Data missing for year 2000',
                        
                        font=dict(family = 'Times New Roman',
                                  size = 20,
                                  color = 'white'), 
                        
                        bgcolor = 'purple',
                        
                        showarrow = False
                       )
                  )


# #### Add the annotations to our layout

# In[18]:


layout['annotations'] = annotations


# #### Plot the figure with the data and layout with annotations

# In[19]:


fig = dict(data=data, 
           layout=layout)

offline.iplot(fig)


# In[ ]:




