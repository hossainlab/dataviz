#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
from plotly import graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# ### Drawing shapes
# Here we plot a rectangle using the following attributes:
# * <b>type</b> sets the type of shape. Shapes can be rect, line, circle etc.
# * <b>xref and yref</b> values determine whether absolute or relative (on a scale of 0 to 1) coordinates are used. Values of 'x' and 'y'</b> mean that absolute values of the x and y coordinates will be used
# * <b>x0,y0,x1,y1</b> represent the left, bottom, right and top extents of the rectangle
# * <b>line</b> will format the bounding line of the rectangle
# * <b>fillcolor</b> determines the fill color for the rectangle

# In[2]:


rect = {'type': 'rect',
        'xref': 'x',
        'yref': 'y',
        'x0': 1,
        'y0': 1,
        'x1': 2,
        'y1': 3,

        'line': {'color': 'blue',
                   'width': 3,
                  },

        'fillcolor': 'cyan'
         }


# #### Plot a circle using a relative scale
# Setting the xref and yref to 'paper' means that we specify a positional value in the 0-1 range. Here 0 is the left or bottom of the axes, 1 is the right or top.
# 
# For a circle, the x0,y0,x1,y1 values represent the extent of the circle - which in our case is not as much a circle as a skewed circle as the width is 0.3 units and the height is 0.8 units. The centre of the circle will have x = (x1-x0)/2 and y = (y1-y0)/2

# In[3]:


circ = {'type': 'circle',
        'xref': 'paper',
        'yref': 'paper',
        'x0': 0.5,
        'y0': 0,
        'x1': 0.8,
        'y1': 0.8,

        'line': {'color': 'green',
               'width': 3,
              },

        'fillcolor': 'honeydew',
              }


# #### Define the layout
# We set the range for the axes and add the shapes to the layout. Note that we have been using a dictionary format to define all these objects

# In[4]:


layout = {'xaxis': {'range': [0, 5]},
          
          'yaxis': {'range': [0, 5]},
          
          'shapes': [rect, circ]}


# #### Add text annotations to the plot
# We can use the Scatter object to define text annotations. Here, we use absolute coordinates which represent the center of the text annotations.

# In[5]:


trace = go.Scatter(x=[1.5, 3],
                   y=[4, 4.5],
                   
                   text=['Using absolute coordinates',
                         'Using relative coordinates'],
                   
                   mode='text',
)

data = [trace]


# #### Plot the figure with the two shapes
# 

# In[6]:


fig = {
    'data': data,
    'layout': layout,
}

offline.iplot(fig)


# ### SVG Notation to draw shapes
# We can use SVG notation to plot various shapes in Plotly

# #### Plot a triangle
# * The shape will be of type 'path'
# * The path contains the SVG Notation:
#  * M will Move the cursor to the point listed after it
#  * L will plot a line from the current cursor location to the point following it
#  * Z will close the shape by drawing a line from the current cursor to the first point

# In[7]:


triangle = {'type': 'path',
            
            'path': ' M 1,1 L 1,4 L 4,1 Z',
            
            'fillcolor': 'lightgrey',
            'line': {'color': 'grey'}
           }


# #### Plot a complex shape
# Here, in addition to plotting lines we plot a quadratic bezier curve. While a line requires two points (start and end), a quadratic bezier curve requires 3 - start, control point, end. 
# 
# The Quadratic bezier curve is denoted by Q and has two points following it - the control point and end point. The start point is where the cursor is.

# In[11]:


odd_shape = {'type': 'path',
            
             'path': ' M 6,4 L 5,6 L 5,8 Q 6,10, 8,8 L 7,4 Z',
            
             'fillcolor': 'tan',
             'line': {'color': 'chocolate'}
           }


# #### Define the layout
# This includes both the shapes we just defined

# In[12]:


layout = {'xaxis': {'range': [0, 10]},
          
          'yaxis': {'range': [0, 10]},
          
          'shapes': [triangle, odd_shape]}


# #### Plot the figure
# Here, we leave the data empty

# In[13]:


fig = {
    'data': [{}],
    'layout': layout,
}

offline.iplot(fig)


# In[ ]:





# In[ ]:




