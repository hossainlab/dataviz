#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Create a figure object
# A figure object represents the plot figure. This can be manipulated in a number of ways. <br />
# Parts of a figure can be viewed here: https://matplotlib.org/tutorials/introductory/usage.html#parts-of-a-figure

# #### Add an axis to the figure
# Add an axes at position rect [left, bottom, width, height] where all quantities are in fractions of figure width and height.
# 

# In[35]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

plt.show()


# In[31]:


type(ax)


# #### Create 2 axes in the figure
# 
# [left, bottom, width, height]
# 
# * Both axes begin at the left of the figure (position 0)
# * The top of the first axis is at 60% of the total height of the figure
# * The bottom of the second axis is at 40% of the total height of the figure
# * The first axis takes up the entire width of the figure
# * The second axis uses 80% of the figure width
# * Both axes only take up 40% of the height of the figure

# In[36]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0.6, 1, 0.4])

ax2 = fig.add_axes([0, 0, 0.8, 0.4])

plt.show()


# #### Plot lines on each of the axes
# * Draw a sine and cosine curve on the axes

# In[37]:


x = np.linspace(start=0, stop=10, num=50)


# In[38]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0.6, 1, 0.4])
ax2 = fig.add_axes([0, 0, 0.8, 0.4])

ax1.plot(x, np.sin(x))

ax2.plot(x, np.cos(x))

plt.show()


# #### Add labels to the axes
# * Here the set_xlabel and set_ylabel functions need to be used

# In[39]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0.6, 1, 0.4])
ax2 = fig.add_axes([0, 0, 0.8, 0.4])

ax1.plot(x, np.sin(x))
ax1.set_xlabel('x', fontsize=15, color='r')
ax1.set_ylabel('sin(x)', fontsize=15, color='r')

ax2.plot(x, np.cos(x))
ax2.set_xlabel('x', fontsize=15, color='r')
ax2.set_ylabel('cos(x)', fontsize=15, color='r')

plt.show()


# #### Placement of axes
# It's also possible to have axes overlap <br />
# Potentially this can be done when you want to view another plot for reference 

# In[40]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])

ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

plt.show()


# #### Figure size
# * Use the figure size parameter to set the width,height in inches
# * The figure size is passed as a tuple

# In[41]:


fig = plt.figure(figsize=(8,8))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

plt.show()


# ### Subplots
# * Each figure can contain a number of subplots
# * A subplot is of type AxesSubplot which is derived from Axes
# * A subplot is thus an instance of matplotlib.axes._axes.Axes

# #### The add_subplot() function
# The Figure object has an add subplot function which can be called with a 3-digit integer as argument (e.g. 221) or alternatively three separate integers (2,2,1). If the three integers are R, C, and P in order, the subplot will take the Pth position on a grid with R rows and C columns <br />
# The call below will create a subplot in the 1st position of a 2x2 grid

# In[48]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)

plt.show()


# In[49]:


type(ax1)


# In[50]:


isinstance(ax1, matplotlib.axes._axes.Axes)


# In[56]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])

plt.show()


# #### A figure with multiple subplots

# In[57]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))


# In[58]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))

ax3 = fig.add_subplot(223)
ax3.plot(x, np.cos(x))


# #### Add the 3rd subplot to position #4

# In[59]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))

ax3 = fig.add_subplot(224)
ax3.plot(x, np.cos(x))

plt.show()


# #### The subplot must be added to a valid position 

# In[60]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(225)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

plt.show()


# ### Using subplot2grid
# This is another way to specify the position of a subplot in a matrix/grid:
# * the first parameter takes in a tuple specifying the (numRows, numColumns)
# * The second parameter is a tuple with the axis' coordinates in the grid. Here, (0,0) is the top-left

# #### We add the sine curve to the (0,0) position

# In[61]:


ax1 = plt.subplot2grid((2, 3), (0, 0))
ax1.plot(x, np.sin(x))
ax1.set_label('sine curve')

ax2 = plt.subplot2grid((2, 3), (0, 1))
ax2.plot(x, np.cos(x))
ax2.set_label('cos curve')

ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=2)
ax3.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax3.set_label('straight line')

ax4 = plt.subplot2grid((2, 3), (1, 0), colspan=2)

ax4.plot(x, np.exp2(x))
ax4.yaxis.tick_right()

ax4.set_label('exponential curve')


# #### Use the plt.subplots() function to return a figure and subplot
# * Use a single function call to get both the figure object and an AxesSubplot object in one shot

# In[62]:


fig, ax = plt.subplots()


# In[63]:


type(fig)


# In[64]:


type(ax)


# In[ ]:




