#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objs as go


# In[2]:


import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Define the data for our plot
# Here, we use the Bar graph object to set the X and Y values. The data list is populated with the single trace which is the Bar Chart.
# 
# Assume we are shop which supplies delicious desserts

# In[3]:


data = [go.Bar(x=['chocolates', 'cakes', 'muffins'],
               y=[50, 14, 35])]


# In[4]:


offline.iplot(data)


# ### Grouped bars

# Assume we have made 2 orders for the desserts. 
# 
# We would like to view the order quantities for the items in each order side by side. For this, we created a grouped bar graph.

# In[5]:


trace1 = go.Bar(x=['chocolates', 'cakes', 'muffins'],
                y=[50, 14, 35],
                name='Order #1')


# In[6]:


trace2 = go.Bar(x=['chocolates', 'cakes', 'muffins'],
                y=[30, 18, 29],
                name='Order #2'
)


# In[ ]:


data = [trace1, trace2]


# #### Define the layout
# Here we need to set barmode to 'group' in order to view a grouped bar graph

# In[8]:


layout = go.Layout(barmode = 'group')


# #### Plot the graph
# Hover over each of the bars to view the corresponding data. A legend is also automatically generated.

# In[9]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# ### Stacked Bar Chart
# Instead of having the two traces side by side, the bars from the traces are stacked to show a cumulative value. 

# In[13]:


trace1 = go.Bar(x=['chocolates', 'cakes', 'muffins'],
                y=[50, 14, 35],
                name='Order #1')

trace2 = go.Bar(x=['chocolates', 'cakes', 'muffins'],
                y=[30, 18, 29],
                name='Order #2'
)

data = [trace1, trace2]


# In[14]:


layout = go.Layout(barmode = 'stack')


# In[15]:


fig = go.Figure(data = data, 
                layout = layout)

offline.iplot(fig)


# ### Customising the Bar Graph
# We can adjust the color, width of the bars and add text labels
# 

# #### Define the new trace
# Aside from the bars which we drew at first, we configure the following:
# * The width of each bar (in axis units). Can either be a list (where the widths are picked in rotation) or a single number (which applies to all bars)
# * The color of each bar in the trace (can again be a number or a list)
# * The text associated with each bar (set to the y value for the order quantity)
# * The position of the text (can be either 'inside', 'outside', 'auto' or 'none'). The available options for textposition will vary according to the object being plotted. These are the options for Bar

# In[8]:


x = ['chocolates', 'cakes', 'muffins']

y = [50, 14, 35]


# In[9]:


trace = go.Bar(x = x,
               y = y,
               
               width = [0.5, 1, 0.7],
               
               marker = dict(color = ['chocolate', 'wheat', 'yellow']),
               
               text = y,
               textposition = 'inside'
)


# In[10]:


data = [trace]


# #### Define the layout
# We add a few more customizations here:
# * We set the font family and font size for the title
# * We angle the tick labels on the X axis

# In[11]:


layout = go.Layout(title='Dessert Order',
                   
                   titlefont = dict(family = 'Arial', size = 15),
                   
                   xaxis = dict(tickangle = 30))


# In[12]:


fig = go.Figure(data = data, 
                layout = layout)

offline.iplot(fig)


# In[ ]:





# In[ ]:





# In[ ]:




