#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# ## Two Y-Axes
# It is often useful to view two different plots - which have the same X axis values, but different Y values - together. In such instances, we can use two Y axes to visualize the two plots.

# #### Generate the first trace

# In[2]:


trace0 = go.Scatter(x = [1, 2, 3], 
                    y = [10,20,30],
                    
                    name = 'yaxis data'
                   )


# #### Create a second trace and map to a second Y axis
# When we set yaxis to 'y2' (the default is 'y'), it means that this axis is a associated with the <b>yaxis2</b> attribute in the layout definition (which we will see shortly)

# In[3]:


trace1 = go.Scatter(x = [5, 6, 7],
                    y = [4, 5, 8],
                    
                    name = 'yaxis2 data',
                    
                    yaxis = 'y2'
)


# #### The data for our plot includes the lines from the two traces

# In[4]:


data = [trace0, trace1]


# #### Define the layout which includes the second Y axis
# <b>yaxis2</b> is set to be an overlay on the Y axis which means it will become a second Y axis. We set its position to be on the right side of the axes. 
# 
# Note that we can overlay the X axis as well and place axes on the left, right, top and bottom depending on which axis is being overlayed.

# In[5]:


layout = go.Layout(title = 'Double Y Axis Example',
                   yaxis = dict(title = 'Default Y Axis'),
                   
                   yaxis2 = dict(title = 'Second Y Axis',
                                 titlefont = dict(color='orange'),
                               
                                 overlaying = 'y',
                                 side = 'right'
                              )
                  )


# #### Plot the figure with the two Y axes

# In[6]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# #### We can have more than two Y axes
# We generate a third trace and map it to yaxis3 in the layout definition by setting its yaxis value to 'y3'.
# 
# We redefine our data

# In[7]:


trace2 = go.Scatter(x = [8, 9, 12],
                    y = [120, 140, 150],
                    
                    name = 'yaxis3 data',
                    
                    yaxis = 'y3'
)


# #### Redefine our data to include the 3 traces

# In[8]:


data = [trace0, trace1, trace2]


# #### Define the new layout to include the 3rd Y axis
# There is a minor difference between this and the addition of the second axis. This is because if we place the 3rd axis on the right of the plot, as with the 2nd axis, they will overlap. 
# 
# We set the value of the <b>anchor</b> attribute for the 3rd axis to 'free'. This allows us to specify the position of the axis on a relative scale along the opposite axis (i.e. a Y axis's posion on the X axis). Here we place this 3rd axis 90% of the way to the right along the X axis.

# In[9]:


layout = go.Layout(title = 'Three Y Axes',
                   yaxis = dict(title='Default Y Axis'),
                   
                   yaxis2 = dict(title='Second Y Axis',
                                 titlefont=dict(color='orange'),
                               
                                 overlaying='y',
                                 side='right'
                              ),
                   
                   yaxis3 = dict(title='Third Y Axis',
                                 titlefont=dict(color='green'),
                               
                                 overlaying='y',
                                 side='right',
                                 
                                 anchor = 'free',
                                 position = 0.9
                              )
                  )


# In[10]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# ## Avocado dataset
# This dataset contains the production and price (per piece) of various kinds of avocados from different regions in the United States between Jan 2014 and March 2018.
# 
# Download the dataset here: https://www.kaggle.com/neuromusic/avocado-prices

# In[11]:


data = pd.read_csv('datasets/avocado.csv')
data.head()


# #### We restrict the data under consideration
# To get unique dates in our series, we restrict our data to organic avocados from California

# In[12]:


data_ca = data.loc[(data['region'] == 'California') & (data['type'] == 'organic')]


# #### We sort the data by date
# This is generate a meaningful time series

# In[13]:


data_ca = data_ca.sort_values(by = ['Date'])
data_ca.head()


# #### Generate a trace for the avocado average price

# In[14]:


priceTrace = go.Scatter(x = data_ca['Date'],
                        y = data_ca['AveragePrice'],
                    
                        name = 'Average Price'
)


# #### Create a trace for the avocado production
# This will be represented by the 2nd Y axis

# In[15]:


volumeTrace = go.Scatter(x = data_ca['Date'],
                         y = data_ca['Total Volume'],
                    
                         name = 'Total Volume',
                         yaxis = 'y2'
)


# #### The data for the plot includes both the price and volume traces

# In[16]:


avocadoData = [priceTrace, volumeTrace]


# #### Define the layout
# The second Y axis will be on the right, and its title text is in orange

# In[17]:


avocadoLayout = go.Layout(title = 'Avocado Production and Prices',
                          yaxis = dict(title='Average Price'),
                   
                          yaxis2 = dict(title = 'Number of Avocados sold',
                                        titlefont = dict(color = 'orange'),

                                        overlaying = 'y',
                                        side = 'right'
                                )
    
)


# #### Plot the figure
# Notice how there is an inverse relationship between produced quantity and average price per avocado

# In[18]:


fig = go.Figure(data=avocadoData, 
                layout=avocadoLayout)

offline.iplot(fig)


# In[ ]:




