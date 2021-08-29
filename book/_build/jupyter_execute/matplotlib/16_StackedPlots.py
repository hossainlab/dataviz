#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Use data about annual visits to some US national parks 
# Data obtained from: https://irma.nps.gov/Stats/Reports/Park
# 
# Number of annual visits in 3 US National parks from 1961-2017 - same data used in the Histograms demo

# In[2]:


np_data= pd.read_csv('datasets/national_parks.csv')
np_data.head()


# #### Define the data to be used in the X axis

# In[3]:


x = np_data['Year']


# #### Use Numpy's vstack method to create a vertical stack
# This will create a 2-D array with the data for number of annual visitors to each park stacked on top of each other. We end up with 3 arrays in the stack - one for each park

# In[4]:


y = np.vstack([np_data['Badlands'], 
               np_data['GrandCanyon'], 
               np_data['BryceCanyon']])
y


# #### Define the labels for each stack item

# In[5]:


labels = ['Badlands', 
          'GrandCanyon', 
          'BryceCanyon']


# #### Plot the Stackplot
# We just pass in the X values along with our stack of y values. We also place a legend on this plot:
# * This plot allows us to view the change in the number of visitors to each park over time
# * We also get to see the total visitors to all these parks put together
# * Notice how the Badlands has drawn a steady number of visitors over the time period, while the others have viewed an increase

# In[6]:


plt.stackplot(x, y, 
              labels=labels)

plt.legend(loc='upper left')

plt.show()


# #### Specify the colors to use in the Stackplot
# We define a list of colors to use

# In[7]:


colors = ['sandybrown', 
          'tomato', 
          'skyblue']


# #### Plot the new Stackplot
# * Make use of the colors list we have just defined
# * Set an edge color used to separate each shape in the stackplot

# In[8]:


plt.stackplot(x, y, 
              labels=labels,
              colors=colors, 
              edgecolor='grey')

plt.legend(loc='upper left')

plt.show()


# ### Stem Plots
# These can also be used to visualize data over time. However, since this also helps us view negative numbers, we can use it to plot a slightly different set of data 

# #### Modify the national parks data to show the difference in the number of visitors from the previous year
# Use the pandas dataframe.diff() function to get the difference in value from the one in the previous row. We only do this for the park visitor information and not for the Year column

# In[9]:


np_data[['Badlands', 
         'GrandCanyon',
         'BryceCanyon']] = np_data[['Badlands', 
                                    'GrandCanyon',
                                    'BryceCanyon']].diff()

np_data.head()


# #### Analyze the fluctuations in the visits to Badlands National Park

# In[10]:


plt.figure(figsize=(10,6))

plt.stem(np_data['Year'],
         np_data['Badlands'])

plt.title('Change in Number of Visitors')

plt.show()


# #### Styling the Stem Plot
# * The first alphabets used for the markerfmt, linefmt and basefmt represent colours
# * After that, the characters represent the type of line/marker
# * '\_' represents a horizontal line
# 
# Objects formatted:
# * markerfmt is the marker appearing at the top of the stems
# * linefmt represents the stems themselves
# * basefmt is the base line - the horizontal one drawn at 0

# In[11]:


plt.figure(figsize=(10,6))

plt.stem(np_data['Year'],
         np_data['Badlands'],
         markerfmt = 'r_',
         linefmt = 'g--',
         basefmt = 'b:')

plt.title('Change in Number of Visitors')

plt.show()


# In[ ]:




