#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install plotly --upgrade')


# In[ ]:



import plotly
plotly.__version__


# #### Plotly's offline module
# The offline module allows interactive plots to be created offline (as opposed to saving them online in one's Plotly account)

# In[2]:


import plotly.offline as offline


# #### The plot() function will create a plot on your local storage and open it up in a browser
# The argument to supply is a figure or data object which is a subclass of a python dictionary. The values which are needed for a plot are the x and y coordinates of the points. 
# 
# This will generate a Plotly scatter plot with a line connecting the points supplied.

# In[3]:


offline.plot([{'x': [1, 3, 6], 
               'y': [3, 1, 5]}])


# #### Generate the plot within the Jupyter notebook
# In order to view the plot inline within the notebook, we need to set plotly to run in notebook mode

# In[4]:


offline.init_notebook_mode(connected=True)


# #### Use the iplot function in order to plot the line inline
# The same plot we generated earlier, but within our notebook. Notice that this is an interactive plot which supplies several options including:
# * Download the plot as a png file
# * Editing the plot in Plotly's own editing tool - Chart Studio
# * Zooming in and out
# * Selecting a section of the plot using a box select or lasso select tool

# In[5]:


offline.iplot([{'x': [1, 3, 6], 
                'y': [3, 1, 5]}])


# #### The X coordinates cane be inferred
# If the X Coordinates are not supplied explicitly, they are set to the index of the y coordinates. In this case the x coordinates are presumed to be [0,1,2]

# In[6]:


offline.iplot([{'y': [3, 1, 5]}])


# #### The Y coordinates can also be inferred
# This time we only supply the X coordinates, and the Y coordinates are set to [0,1,2]

# In[7]:


offline.iplot([{'x': [3, 1, 5]}])


# #### Use Python's help function to get the documentation for Plotly functions
# The online documentation for Plotly contains examples, but does not list details such as the parameters for a function. For that, use Python's help() for Plotly functions as well as modules and objects.
# 
# The online documentation is better for objects though. 

# In[8]:


help(offline.iplot)


# In[ ]:




