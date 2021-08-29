#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Create a list of all the continents
# We don't consider Antarctica here

# In[2]:


continents = ['Asia', 
              'Africa', 
              'Europe', 
              'North America', 
              'Oceania', 
              'South America']


# #### A list of the population for each continent (in millions)

# In[3]:


populations = [4436, 1216, 739, 579, 40, 423]


# #### A simple pie chart
# We only need to supply the labels and values needed for the plot

# In[19]:


trace = go.Pie(labels = continents, 
               values = populations,
              )


# #### Plot the pie chart
# * The color for each wedge will be picked from a default color palette
# * The percentage for each wedge is displayed by default
# * For wedges representing a very tiny value, Plotly is smart enough to place the text outside
# * A legend appears by default

# In[20]:


data = [trace]

offline.iplot(data)


# ### Styled Pie Chart
# We can customize the pie chart by formatting the wedges and the text displayed

# #### Create a list of colors
# These will be used to represent the different continents on the chart

# In[ ]:


colors = ['burlywood', 'silver', 'olive', 'skyblue', 'violet', 'crimson' ]


# #### Define the pie chart
# * we set the hoverinfo to show the wedge label along with the percentage value for the sector
# * we explicitly set the text inside the wedge to display value (can also be 'percent', 'label' or a combination)
# * the font for the displayed text can be formatted
# * marker represents the wedges of the pie chart. We configure it to:
#  * use the list of colors we defined
#  * use a dark grey line at the boundaries
#  * set the width of the boundary line
# * the value of hole will create a hole in the pie chart. The value can be between 0 and 1 and represents the width of the hole relative to the whole pie

# In[21]:


trace = go.Pie(labels = continents, 
               values = populations,
               
               hoverinfo = 'label+percent', 
               
               textinfo = 'value', 
               textfont = dict(size = 20),
               
               marker = dict(colors = colors,
                             line = dict(color = 'dimgrey', 
                                         width = 2)
                            ), 
               hole = 0.4
              )


# In[22]:


data = [trace]

offline.iplot(data)


# In[ ]:




