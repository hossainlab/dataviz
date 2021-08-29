#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# ### Load a dataset
# Assume this is the breakdown of the investment portfolio of a fictitious mutual fund

# In[2]:


data= pd.read_csv('datasets/sector_weighting.csv')
data


# ### Pie Chart
# Here, we plot a basic pie chart with the percentage values and the sector names as labels. Note that we don't even need labels to draw a chart, though it's meaningless without them. 
# 
# This chart though is a little skewed due to the X axis being longer on the screen.

# In[3]:


plt.pie(data['Percentage'], 
        labels=data['Sector'])

plt.show()


# #### Set the aspect of each axis to be equal
# Similar to the set_aspect function for an axis, we can set the define the aspect of this plot to be equal with the plt.axis() function

# In[4]:


plt.pie(data['Percentage'], 
        labels=data['Sector'])

plt.axis('equal')

plt.show()


# #### Pie chart customizations
# We add some customizations to this chart. So far, the colors have been picked by cycling through the default color palette. We now define a set of colours to use. 

# In[5]:


colors = ['deeppink', 'aqua', 'magenta', 'silver','lime']


# #### Draw the pie chart with the new colour palette and show percentage values
# We set the values for the colors and autopct properties. The latter sets the format for the values to be displayed. 

# In[6]:


plt.pie(data['Percentage'], 
        labels=data['Sector'], 
        colors=colors, 
        autopct='%.2f')

plt.axis('equal')

plt.show()


# #### Re-orienting the pie chart sectors
# The wedges of the chart are drawn starting from the 90 degree (or 3 0'clock) position and going anti-clockwise. Here we offset the start position by 90 degrees so that it starts in the 12 o'clock position and goes clockwise

# In[7]:


plt.pie(data['Percentage'], 
        labels=data['Sector'], 
        colors=colors, 
        autopct='%.2f',
        startangle=90, 
        counterclock=False)

plt.axis('equal')

plt.show()


# #### The explode property
# To highlight a particular wedge (or wedges) of the pie chart, we use explode to separate it from the rest of the chart. 
# 
# The value for "explode" represents the fraction of the radius with which to offset each wedge. Here we "explode" the wedges for Beverages and Tobacco by 0.1 and 0.3 respectively

# In[8]:


explode = (0, 0.1, 0, 0.3, 0)


# In[9]:


plt.pie(data['Percentage'], 
        labels=data['Sector'], 
        colors=colors, 
        autopct='%.2f',
        explode=explode)

plt.axis('equal')

plt.show()


# ### Pie chart components
# A pie chart comprises the following pieces:
# * <b>wedges:</b> A list of Patch objects representing each wedge
# * <b>texts:</b> List of Text objects representing the labels
# * <b>autotexts:</b> List of Text objects for the numeric values - this is only availabe if the autopct value for the pie chart is not None

# In[10]:


wedges, texts, autotexts = plt.pie(data['Percentage'], 
                                    labels=data['Sector'], 
                                    colors=colors, 
                                    autopct='%.2f',
                                    explode=explode)

plt.axis('equal')

print('Wedges: ', wedges)
print('Texts: ', texts)
print('Autotexts: ', autotexts)


# #### Formatting the individual components of the pie chart
# As an example, we format the wedge and texts representing "Beverages"

# In[11]:


wedges, texts, autotexts = plt.pie(data['Percentage'], 
                                    labels=data['Sector'], 
                                    colors=colors, 
                                    autopct='%.2f',
                                    explode=explode)

plt.axis('equal')

wedges[1].set(edgecolor='blue', linewidth=2)

texts[1].set(family='cursive', size=20)

autotexts[1].set(weight='bold', size=15)


# In[ ]:




