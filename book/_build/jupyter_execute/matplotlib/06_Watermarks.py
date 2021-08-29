#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# In[4]:


fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4],
        [2, 4, 6, 8])


# #### Add a text watermark to the subplot
# * First two arguments represent the x and y coordinates for the the text - specifically the ha and va (so bottom left of the text)
# * The next argument is the actual text
# * ha and va are represent the horizontal and vertical alignments
# * alpha is the degree of transparency

# In[5]:


fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4],
        [2, 4, 6, 8])

ax.text(1, 4, 'Do not distribute',
        fontsize=30, 
        color='red',
        ha='left', 
        va='bottom', 
        alpha=0.5)


# #### See how changing ha and va affects text placement

# In[6]:


fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4],
        [2, 4, 6, 8])

ax.text(1, 4, 'Do not distribute',
        fontsize=30, 
        color='red',
        ha='right', 
        va='top', 
        alpha=0.5)


# ### Watermarks for axes and figures
# * Watermarks can be added to individual axes of a figure
# * There can also be one for the figure itself

# ##### Define x values for use in a sine curve

# In[7]:


x = np.linspace(start=0, stop=10, num=50)


# #### Create a subplot with a watermark
# Here, the x and y coordinates of the plot will be specified for text placement, as seen above

# In[8]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

ax1.text(1, 4, 'Do not distribute',
        fontsize=20, 
        color='red',
        ha='left', 
        va='bottom', 
        alpha=0.5)


# ##### Add two more subplots
# These do not have watermarks

# In[9]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

ax1.text(1, 4, 'Do not distribute',
        fontsize=20, 
        color='red',
        ha='left', 
        va='bottom', 
        alpha=0.5)

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))

ax3 = fig.add_subplot(223)
ax3.plot(x, np.cos(x))


# #### Recreate the same subplots in a new figure
# Including the subplot watermark in the first subplot

# #### Add a watermark to the figure
# The coordinates specified are on a 0-1 scale

# In[11]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

ax1.text(1, 4, 'Do not distribute',
        fontsize=20, 
        color='red',
        ha='left', 
        va='bottom', 
        alpha=0.5)

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))

ax3 = fig.add_subplot(223)
ax3.plot(x, np.cos(x))

fig.text(0.1, 0.5, 'Property of Pluralsight',
         fontsize=40, 
         color='gray',
         ha='left', 
         va='bottom', 
         alpha=0.3)


# ### Image watermark
# First import the image and cbook objects

# In[20]:


import matplotlib.image as image
import matplotlib.cbook as cbook


# In[23]:


get_ipython().system('pwd')


# In[28]:


datafile = cbook.get_sample_data(
    '/Users/jananiravi/Desktop/iMovieLibrary/Pluralsight/Matplotlib/Demos/matplotlib/pluralsight_logo.png', 
    asfileobj=False)


# In[29]:


im = image.imread(datafile)


# In[30]:


fig = plt.figure(figsize=(8,8)) 

ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3, 4], 
         [2, 4, 6, 8])
ax1.set_label('straight line')

ax1.text(1, 4, 'Do not distribute',
        fontsize=20, 
        color='red',
        ha='left', 
        va='bottom', 
        alpha=0.5)

ax2 = fig.add_subplot(222)
ax2.plot(x, np.sin(x))

ax3 = fig.add_subplot(223)
ax3.plot(x, np.cos(x))

fig.figimage(im, 100, 150, 
             zorder=3, 
             alpha=0.3)


# In[ ]:




