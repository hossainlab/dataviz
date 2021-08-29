#!/usr/bin/env python
# coding: utf-8

# ### Backends
# In Matplotlib the term "frontend" is used to refer to user-facing code. While the "backend" is the part of Matplotlib which does the hard work of plotting the figure. 
# 
# Matplotlib can be used in different environments in the python shell, with another graphical user interface - the ability of matplotlib to support these use cases is due to the different backends available
# 
# #### Types of backends
# * User Interface backends: These are interactive backends where the figure plotted is interactive. E.g. nbagg, qt4
# * Hard Copy backends: These are non-interactive and effectively render image files. E.g. png, svg, pdf
# 
# There are multiple backends which will be available to you, and can be listed by running this command. The list will likely vary for each user depending on their OS and the tools installed. Note that even though some of these backends are listed, they may need to be installed before they are used.

# In[1]:


get_ipython().run_line_magic('matplotlib', '--list')


# #### Import the Matplotlib library

# In[2]:


import matplotlib


# #### Check which mode you are running in

# In[3]:


matplotlib.is_interactive()


# #### Since we will be using an interactive plot, we switch to interactive mode

# In[4]:


matplotlib.interactive(True)


# #### Check what your backend is
# An inline backend implies that the matplotlib figures will be plotted inline within your notebook. But this is not an interactive backend

# In[5]:


matplotlib.get_backend()


# #### Switch to a different backend
# The nbagg backend enables interactive figures in a live IPython notebook session

# In[6]:


matplotlib.use('nbagg')


# In[7]:


matplotlib.get_backend()


# In[8]:


import matplotlib.pyplot as plt

plt.ion()
matplotlib.is_interactive()


# #### Render the interactive plot
# This figure offers features such as zooming in on portions of the plot and navigating between different views.

# In[9]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16])


# #### Set a title for the plot
# This will update our interactive plot to include the title

# In[10]:


plt.title('Interactive plot')


# In[ ]:





# In[ ]:




