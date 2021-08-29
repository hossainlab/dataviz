#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
from plotly import graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Load the data
# Consider an e-commerce website which needs to track customer behaviour. It has defined different phases which a customer can be in when making a purchase starting from Viewing their cart contents. 
# 
# As these steps can only be followed in sequence, the number of customers who get to a particular phase are always a subset of those who entered the previous phase.

# In[2]:


import pandas as pd

data_table = pd.read_csv('datasets/customer_info.csv')
data_table


# #### Store the phases and values for each phase in lists
# These will be referenced frequently later on

# In[3]:


phases = data_table['Phases']

values = data_table['Values']


# #### Set the colors to use in the funnel chart
# Define colors which will be used to represent the phases in the funnel chart

# In[4]:


colors = ['Pink', 'Blue', 'Yellow', 'Purple', 'Green']


# #### Store the number of phases in a variable and define the max funnel width
# The number of phases will be used frequently, so we store it in a variable. The max width for the funnel will be 400 pixels.
# 
# A funnel section will be drawn using Plotly shapes, in the shape of a Rectangle or Isosceles Trapezoid depending on the value of the next phase. The phase having maximum value will have the width equal to the plot.

# In[5]:


num_phases = len(phases)

plot_width = 400


# #### Set the height for each funnel section and the gap in between
# Each section will be 100 pixels high with a 10 pixel gap in between

# In[6]:


section_height = 100

section_gap = 10


# #### Define the widths for each section in the funnel chart
# The width of the section represents the value for each phase (the number of customers in that phase) the height is constant for each section, but the width varies.
# 
# Here, we set the width of each funnel section relative to the plot width

# In[7]:


unit_width = plot_width / max(values)

phase_widths = [int(value * unit_width) for value in values]

phase_widths


# #### Get the plot height
# The plot height depends on the number of sections - equal to the sum of the heights of each section plus the total gaps between the sections.
# 
# The number of gaps will be one less than the number of sections.

# In[8]:


height = section_height * num_phases + section_gap * (num_phases - 1)
height


# #### Generate the points for the first section in the funnel
# Consider the X axis centered at 0. The funnel chart for the first (top) section should have a width representing that phase at the top (phase_widths[0]) and should taper to the width of the next phase (phase_width[1]) at the bottom. 
# 
# The height of the section is fixed (100), so the height ranges from the current height (height) at the top to (height - section_height) at the bottom.

# In[9]:


points = points = [phase_widths[0] / 2, height, phase_widths[1] / 2, height - section_height]
points


# #### Define the path in order to draw the section
# We use the SVG path in order to plot this trapezium/trapezoid

# In[10]:


path = 'M {0},{1} L {2},{3} L -{2},{3} L -{0},{1} Z'.format(*points)
path


# #### Define the shape using the SVG path

# In[11]:


section = {'type': 'path',
           'path': path,
           'fillcolor': colors[0],
           'line': {'color': colors[0]}
          }


# #### To view this single section, we define a layout
# This layout only contains our trapezoid

# In[12]:


layout = go.Layout(shapes = [section])


# #### Plot the figure with only this one section
# This is what a section in a funnel should look like. The top represents the value of this section and it tapers down where the bottome width represents the value of the next section.
# 
# It is just the final section which will be a rectangle

# In[13]:


fig = go.Figure(data=[{}], 
                layout=layout)

offline.iplot(fig)


# #### Define lists which will be used to plot the funnel chart
# We need lists for:
# * Each shape we will plot which includes n-1 trapezoids and 1 rectangle at the bottom
# * The path_list will hold the SVG path for each shape
# * The section_label_heights will be used to set the heights of the text annotations for each section

# In[14]:


shapes = []
path_list = []
y_labels = []


# #### Fill in the SVG Paths and section_label_heights for the sections
# Since the last section will be a rectangle instead of a trapezoid, we need to check whether we are on the last section or not. The tasks we then perform are:
# * Calculate the SVG path for the section and then append it to the path list
# * Add the y coordinate for the text annotations for the section in y_labels
# * Adjust the height to the top of the next section by decrementing its value by (section_height + gap)

# In[15]:


for i in range(num_phases):
    
        if (i == num_phases-1):
                points = [phase_widths[i] / 2, height, phase_widths[i] / 2, height - section_height]
        else:
                points = [phase_widths[i] / 2, height, phase_widths[i+1] / 2, height - section_height]
        
        path = 'M {0},{1} L {2},{3} L -{2},{3} L -{0},{1} Z'.format(*points)
        
        print('\nPoints for Phase %d = %s' %(i, points))
        print('Path for Phase %d = %s' %(i, path))
        
        path_list.append(path)
        
        y_labels.append(height - (section_height / 2))
        
        height = height - (section_height + section_gap)


# #### Generate a list of shapes for the funnel
# This will contain all the section shapes which are set to a color from our colors list

# In[16]:


for i in range(num_phases):

        shape = {'type': 'path',
                 'path': path_list[i],
                 'fillcolor': colors[i],
                 'line': {'color': colors[i]}
                }

        shapes.append(shape)
        
shapes


# 
#      To draw the phase names and values, we are using the text mode in scatter plots. To style the plot, we are hiding the legend and tick labels, and removing the zeroline.

# #### Add the labels for each phase/section
# We apply an offset for the x coordinate of the text annotation so that it does not overlap with the shapes. These annotations will appear on the left of the plot

# In[17]:


label_trace = go.Scatter(x = [-170]*num_phases,
                         
                         y = y_labels,
                         
                         mode = 'text',
                         
                         text = phases
                        )


# #### Enter the phase values
# These will appear on the right of the funnel

# In[18]:


value_trace = go.Scatter(x = [170]*num_phases, 
                         
                         y = y_labels,
                         
                         mode = 'text',
                         
                         text = values
                        )


# In[19]:


data = [label_trace, value_trace]


# #### Define the layout
# We set the following attributes:
# * A title for the chart along with its font size
# * Assign the shapes for the plot
# * Remove the tick labels and zero lines from the plot
# * Deactivate the legend (our traces are the text annotations, so we don't need a legend)

# In[21]:


layout = go.Layout(title = "<b>Funnel Chart</b>",
                   titlefont = dict(size=20),
                   
                   shapes = shapes,
                   
                   showlegend = False,
                   
                   xaxis = dict(showticklabels = False,
                              zeroline = False,
                             ),
                   
                   yaxis = dict(showticklabels = False,
                              zeroline = False
                             )
                  )


# In[22]:


fig = go.Figure(data=data, layout=layout)

offline.iplot(fig)


# In[ ]:





# In[ ]:




