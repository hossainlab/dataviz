#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# ## Sankey Diagrams
# Sankey diagrams are a useful way to display movement between locations/nodes.
# 
# As an example, assume a person has set up a conference in his/her office and has attendees visiting from uptown, midtown and downtown in the city. They enter the office from either the front or rear lobby and then make their way to the conference room.

# #### Create a list for all the locations/nodes

# In[2]:


locations = ['Uptown', 
             'Midtown', 
             'Downtown', 
             'Front Lobby', 
             'Rear Lobby', 
             'Conference Room'
            ]


# #### Define the Sankey diagram
# The nodes will be the locations we have defined above. The ordering of these nodes matters as they will be assigned an index which will be used to define the links in the Sankey diagram.
# 
# The source and target are effectively the nodes at either end of the link. The value represents the weight of the link. So taking the first index of each list, we get (0, 3, 2) - this means 2 people went from Uptown to the Front Lobby. 

# In[3]:


data = go.Sankey(node = dict(label = locations),
                 
                 link = dict(source = [0, 0, 1, 1, 2, 3, 4], 
                             target = [3, 4, 3, 4, 3, 5, 5], 
                             value =  [2, 2, 4, 1, 5, 9, 3]
                            )
                )


# In[4]:


layout =  dict(title = 'Basic Sankey Diagram',
               font = dict(size = 12)
)


# #### Plot the diagram
# We observe that 2 of the attendees seem to have lost their way from the front lobby to the conference room

# In[5]:


fig = dict(data=[data], 
           layout=layout)

offline.iplot(fig)


# #### Using a real dataset
# This dataset tracks the movement of refugees aiming to enter Australia from their countries of origin to the refugee camps in Manus and Nauru and beyond. 
# 
# Download the dataset here: https://github.com/plotly/dash-app-datasets/blob/master/refugee-movement.csv

# In[6]:


import pandas as pd

data = pd.read_csv('datasets/refugee_movement.csv')
data


# #### Plot the Sankey diagram
# Format the nodes:
# * <b>pad</b> determines the amount of padding between the nodes
# * <b>thickness</b> sets the width of the node
# 
# The 'Node, Label' field is meant to be a list of all the nodes contains several nan values in the dataframe. We drop those values when using it in our diagram

# In[7]:


data_trace = go.Sankey(node = dict(pad = 10,
                                   thickness = 30,
                                   
                                   label =  data['Node, Label'].dropna(),
                                   
                                   color = data['Color']),
                       
                       link = dict(source = data['Source'],
                                   target = data['Target'],
                                   value = data['Value'])
                      )


# In[8]:


layout =  dict(title = "Refugee movement through Manus and Nauru")


# In[9]:


fig = dict(data=[data_trace], 
           layout=layout)

offline.iplot(fig)


# In[ ]:




