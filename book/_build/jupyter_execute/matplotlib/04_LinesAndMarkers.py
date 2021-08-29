#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### We start off with the previously seen sine curve

# In[2]:


x = np.linspace(start=0, stop=10, num=50)


# In[3]:


plt.plot(x, np.sin(x))

plt.show()


# #### Having multiple plots in a pyplot
# The colors of each plot is chosen by iterating over a color palette. The default palette is {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'} 

# In[4]:


plt.plot(x, np.sin(x), label='sine curve')
plt.plot(x, np.cos(x), label='cosine curve')

plt.legend()
plt.title('Playing with Plots')

plt.show()


# #### Specifying colors
# We pick the colors of green and magenta for the curves
# * We have specified the full name of the green color
# * Magenta has been specified in shorthand ('g' is short for green) <br />
# 
# The colors and codes for Matplotlib are here:
# https://matplotlib.org/2.0.2/api/colors_api.html
# 
# The full list of named colors is here:
# https://matplotlib.org/examples/color/named_colors.html

# In[5]:


plt.plot(x, np.sin(x), label='sine curve', color='green')
plt.plot(x, np.cos(x), label='cosine curve', color='m')

plt.legend()
plt.title('Playing with Plots')

plt.show()


# ### Formats for lines and markers
# Line formats: https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html <br />
# Marker formats: https://matplotlib.org/1.4.1/api/markers_api.html <br />

# #### Plots need not be lines
# Start off by plotting a random array of 20 numbers

# In[6]:


random_array = np.random.randn(20)


# In[7]:


plt.plot(random_array, 
         color='green')
plt.show()


# #### Line styles
# We can have solid, dashed, dotted or dash-dot lines

# In[8]:


plt.plot(random_array, 
         color='green',
         linestyle=':')
plt.show()


# In[9]:


plt.plot(random_array, 
         color='green',
         linestyle='--')
plt.show()


# #### Adjust the line width
# The default is 1

# In[10]:


plt.plot(random_array, 
         color='green',
         linestyle='--',
         linewidth=3)
plt.show()


# #### We use markers to denote the points
# The 'd' denotes small diamonds. For all the marker styles check out this page: <br />
# https://matplotlib.org/1.4.1/api/markers_api.html

# In[11]:


plt.plot(random_array,
         color='green', 
         marker = 'd')
plt.show()


# #### Adjust the marker size
# Default is 6

# In[12]:


plt.plot(random_array,
         color='green', 
         marker = 'd',
         markersize=10)
plt.show()


# #### Get rid of the line and use only markers

# In[13]:


plt.plot(random_array,
         color='green', 
         marker = 'd',
         linestyle = 'None')
plt.show()


# #### Scatter plots
# These are similar to regular plots but you need to specify the x coordinates. Below we create the same plot as above, but explicitly give the x coordinates as a list of 0-19

# In[14]:


plt.scatter(range(0,20),
            random_array,
            color='green', 
            marker = 'd')
plt.show()


# In[ ]:




