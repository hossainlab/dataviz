#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Obtain a set of random points
# The Y values are a set of random values in the range [0,1000000) <br />
# The X values are simply a sequence from 0 to the number of elements in y

# In[2]:


np.random.seed()


# In[3]:


y = np.random.uniform(low=0.0, high=1000, size=(1000,))
y.sort()

x = np.arange(len(y))


# #### Linear line
# * We plot Y vs X with the scale of Y being linear (which is the default)
# * We also show grid lines on our plot
# * Note how the scales of the axes are linear as we have seen so far

# In[4]:


plt.plot(x, y)

plt.grid(True)

plt.yscale('linear')

plt.show()


# #### Logarithmic scale
# Instead of a specific length of the Y axis corresponding to a specific range of values, we can adjust the scale of the axis where the scale is logarithmic. <br />
# By the default the base of the log scale is 10

# In[5]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('log')

plt.show()


# #### Changing the base of the log scale
# Use the basey property (or basex if you're scaling the X axis) to set the base of the log scale

# In[6]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('log', basey=2)

plt.show()


# #### Using different logarithmic scales on each axis

# In[7]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('log', basey=10)

plt.xscale('log', basex=2)

plt.show()


# #### We use a different distribution this time with negative values
# We use a normal distribution to get a distribution of values with a mean of zero. Most of the values will be in the interval (-100, 100)

# In[8]:


y = 100 * np.random.normal(size=1000)
y.sort()

x = np.arange(len(y))


# In[9]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('linear')

plt.show()


# #### A log scale discards negative values
# Our plot is truncated as the the log of negative numbers cannot be calculated

# In[10]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('log')

plt.show()


# ### Symlog
# This allows us to have a logarithmic scale as well as negative values in our distribution. Note how a lot of the values are near zero (given it's a normal distribution)

# In[11]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('symlog')

plt.show()


# #### linthreshy
# Matplotlib allows one to set a "linear threshold" - a range around zero where the scale of the axis will be linear, and then logarithmic beyond that. <br />
# Here, we say that all values in the range (-10, 10) must be plotted in a linear scale while the remainder of the values will be on a symlog scale. This allows the values in that interval to be spread more evenly on the plot <br />
# Notice that the grid lines for the Y axis don't crowd around 0 as they did previously

# In[12]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('symlog', linthreshy=10)

plt.show()


# ### Logit scale
# This is meant for data between 0 and 1. For that we begin with a new distribution

# In[13]:


y = np.random.uniform(low=0.0, high=1.0, size=(1000,))
y.sort()

x = np.arange(len(y))


# #### Plot the distribution on a linear scale

# In[14]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('linear')

plt.show()


# #### View the data on a logarithmic scale

# In[15]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('log')

plt.show()


# #### For the Logit scale, we need a NullFormatter
# To begin we import a NullFormatter for the Y axis. This is to remove labels on all the ticks on the Y axis (and only retain them on the grid lines). We shall see later why this is required

# In[16]:


from matplotlib.ticker import NullFormatter


# #### Plot the graph
# This scale is similar to a log scale close to zero and to one, and almost linear around 0.5

# In[17]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('logit')
plt.gca().yaxis.set_minor_formatter(NullFormatter())

plt.show()


# #### Plot the line without the NullFormatter
# All the y ticks will be displayed, with the values overlapping each other

# In[18]:


plt.plot(x, y)
plt.grid(True)

plt.yscale('logit')

plt.show()


# In[ ]:




