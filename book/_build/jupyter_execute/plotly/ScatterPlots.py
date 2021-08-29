#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# In[2]:


import plotly.graph_objs as go

import numpy as np


# #### Generate a sets of 200 x and y coordinates
# These will be used in our scatter plot

# In[3]:


n = 200

random_x = np.random.randn(n)

random_y = np.random.randn(n)


# #### Creating a trace from a Plotly Scatter object
# This will generate points using the X and Y coordinates which we supply. The X and Y coordinates are paired by their index. 
# 
# Setting the mode to 'markers' will ensure that only the points are plotted, and are not connected by a line. The default mode is 'lines' where the points are connected by a line in the order of their index. i.e. (x0, y0) to (x1, y1) to (x2, y2) etc.
# 
# The trace or graph is effectively a JSON object containing the details needed for a plot.

# In[4]:


trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

trace


# #### The data supplied for a plotly plot needs to be a list
# This is because we can have multiple traces on the same plot (as we shall soon see)

# In[5]:



data=[trace]


# #### Produce the plot using iplot
# Hover over each point to view the X and Y coordinates of the point

# In[6]:



offline.iplot(data)


# ### Multiple Scatter plots in one plot
# Here we produce multiple graphs on the same plot. We do that by having a single set of x coordinates shared by 3 sets of y coordinates. We space out the y values for each graph so that they do not overlap on the plot. 

# #### Generate the X coordinates
# We will create 50 points in each graph. Start off by creating 50 evenly spaced x values in the interval (0,1). These values are ordered (so that lines connecting them move left to right rather than all over the place)

# In[46]:


n = 50

random_x = np.linspace(0, 1, n)


# #### Generate 3 sets of Y coordinates
# These are spaced with offsets of 5 so that they do not overlap. There is no ordering of values here.

# In[47]:


random_y0 = np.random.randn(n)+5

random_y1 = np.random.randn(n)

random_y2 = np.random.randn(n)-5


# #### The first trace/graph contains only markers
# These will only be points which are not connected by a line. A name is assigned to the trace - this will appear in the legend of the plot

# In[9]:


trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers'
)


# #### The second trace has only a line
# The points are connected by a line, but without markers for the points

# In[10]:



trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines'
)


# #### The third trace has both markers and a connecting line

# In[11]:


trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines+markers'
)


# #### The data for our plot now comprises three traces
# These are all contained in a list which is used by the plot

# In[12]:


data = [trace0, trace1, trace2]


# #### Generate the plot
# Plotly is smart enough to create a legend automatically, though it has assigned some default names for the traces.

# In[13]:


offline.iplot(data)


# # Style Scatter Plots
# We can customize the look of the scatter plots by configuring each of its components. Here, we show how we can define the markers, lines, graph names, the axes and set a title for our plot.
# 
# We also define a layout and figure instead of plotting with only the data. A figure object comprises the data plus a layout.

# #### Define a style for the marker
# Among other attributes, we can set the size and color of markers. There are different ways to set the colors, but here we just use the names of some colors. 
# 
# 

# In[48]:


marker_style = dict(size = 10,
                    color = 'orange')


# #### Define the line style
# Here, we set the color and width

# In[49]:


line_style = dict(width = 3, 
                  color = 'khaki')


# #### Define the first trace
# It's the same as the previous one, but with a customised marker style. We also set a name for the graph which will appear in the legend (instead of "trace 0")

# In[50]:


trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    marker = marker_style,
    name = 'Markers only'
)


# #### The second trace uses the line style
# We also set a name for this trace

# In[51]:


trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines',
    line = line_style,
    name = 'Lines only'
)


# #### Define the third trace
# This one uses both the line style and marker style

# In[52]:


trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines+markers',
    marker = marker_style,
    line = line_style,
    name = 'Markers + Lines'
)


# #### Each plot contains a layout which can be configured
# The layout has several configurable attributes including the title and the axes. For the axes, we set the width for the zero line

# In[53]:


layout = dict(title = 'Styled Scatter',
              yaxis = dict(zerolinewidth = 4),
              xaxis = dict(zerolinewidth = 4)
             )


# #### Define the data for our plot
# Just as before, it contains the 3 traces we have created. This time with the additional styling.

# In[54]:


data = [trace0, trace1, trace2]


# #### Define a figure object
# A figure is simply an object which contains the data and the layout definition for a plot. This time we will plot a figure object instead of a data object.

# In[55]:


fig = dict(data = data, 
           layout = layout)


# #### Plot the figure
# 

# In[56]:


offline.iplot(fig)


# ### Using a color scale
# A color scale will set the color of an object (e.g. a marker) according to a particular value. This will allow the visualization of an extra dimension in a plot (a 3rd dimension in a 2D and 4th in a 3D plot). 

# #### Define x, y and z values
# Similar to the scatter plot we plotted right in the beginning, this time with an added Z dimension

# In[23]:


n = 200

random_x = np.random.randn(n)

random_y = np.random.randn(n)

random_z = np.random.randn(n)


# #### Colorscales
# Plotly uses the Matplotlib colormaps for its colorscales. The list of available colorscales can be found here:
# https://matplotlib.org/examples/color/colormaps_reference.html
# 
# The way this works is that for a given range of values (in our example, the range of Z values) the colorscale is created such that a value will correspond to a color on the colorscale. 

# #### Generate the trace with the details for the colorscale
# Here, the we define our scatter trace to color the markers according to the value of the Z coordinate, and using the colorscale 'Magma'.
# 
# showscale = True will ensure the colorscale is portrayed on the plot.
# 
# We also define the text which will be visible when we hover over a point. We set this to the Z value of the point so that we can match it to the color in the colorscale.

# In[24]:



trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker= dict(size = 14,
                 color = random_z,
                 colorscale = 'Magma',
                 showscale = True),
    text = random_z
)


# In[25]:


data = [trace]


# #### Define the layout
# The Layout can also be defined using the go.Layout object rather than a dictionary.
# 
# By default, when hovering over a graph, the y value is displayed near the cursor, and the x value near the X axis. This is when the hovermode is 'x'.
# 
# Setting the hovermode to 'y' will cause the x value to be displayed at the cursor and y value on the Y axis. We use the 'closest' hovermode to display the (x,y) and hover text of the closest marker from the cursor. 

# In[26]:


layout = go.Layout(title = 'Scatter with Colorscale',
                   hovermode = 'closest')


# #### Define the figure
# Like the layout, there is also a go.Figure object

# In[27]:


fig = go.Figure(data = data, 
                layout = layout)


# #### Plot the data
# Hover over the markers to view the Z value and match it to the colorscale on the right

# In[28]:


offline.iplot(fig)


# 

# #### Import the Pandas library
# This will help us load a dataset

# In[29]:


import pandas as pd


# #### Honey Production dataset
# 
# The dataset can be downloaded from here: https://www.kaggle.com/jessicali9530/honey-production

# In[30]:


honey_data = pd.read_csv('./datasets/honeyproduction.csv')


# #### Preview the data
# 
# The honey dataset shows total honey production, yield per colony etc. for each state In the USA from 1998 to 2012

# In[31]:


honey_data.head()


# #### Generate the trace
# 
# The data we will plot includes:
# * State on the X axis
# * Year on the Y axis
# * Honey production (lbs) represented by a color from the colorscale
# 
# We use the Rainbox colorscale in this example. The opacity of each of the markers can also be set.
# 
# This allows us to assess just by looking at the plot what the honey production was for a particular year for a state. So we can spot any changes in honey production quite easily

# In[32]:


trace= go.Scatter(
    
         x = honey_data['state'],
        
         y = honey_data['year'],
    
         mode = 'markers',
    
         marker = dict(size= 14,
                    color=honey_data['totalprod'],
                    colorscale='Rainbow',
                    showscale=True,
                    opacity= 0.5
                   ),
    
        text = honey_data['totalprod']
)  


# In[33]:



data=[trace]


# #### Define the layout

# In[34]:


layout= go.Layout(
    
    title= 'Honey production the United States',
    
    hovermode= 'closest',
    
    xaxis= dict(title= 'States'),
    
    yaxis=dict(title= 'Honey Production')
)


# In[35]:


fig= go.Figure(data=data, 
               layout=layout)


# In[36]:


offline.iplot(fig)


# In[ ]:





# In[ ]:




