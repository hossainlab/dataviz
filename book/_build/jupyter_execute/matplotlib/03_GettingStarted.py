#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# * Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
# * It is a plotting library for the Python programming language and its numerical mathematics extension NumPy

# <b>Pyplot</b> is a class in matplotlib which is used to create figures and change the characteristics of figures

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# ### Create a simple plot
# The plot() function will take in X and Y coordinates and plots 

# In[2]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16])


# #### We specify the color to use when plotting the line

# In[3]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16],
         color='red')


# #### We re-define the plot with labels for the axes
# The axes will be labeled with the given name in red <br />
# The show() function will display the plot this time as it's been re-defined

# In[4]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16])

plt.xlabel('x', fontsize=15, color='green')
plt.ylabel('2*x', fontsize=15, color='green')


# #### Plot without specifying x coordinates
# * If a single array is passed to the plot function, the array contents are assumed to be y values
# * The index of each value is assumed to be its x value

# In[5]:


plt.plot([4, 8, 12, 16])


# #### Generate a sine wave
# Use numpy to generate the plots for a sine wave and plug those into a Matplotlib plot

# In[6]:


x = np.linspace(start=0, stop=10, num=50)


# In[7]:


plt.plot(x, np.sin(x))

plt.xlabel('x', fontsize=15, color='green')
plt.ylabel('sin(x)', fontsize=15, color='green')


# #### We can format the ticks and the tick labels
# First, we format the Y axis:
# * The little tick markers will be red
# * The tick labels will be green
# * The size of the tick label text will be xx-large

# In[8]:


plt.tick_params(axis='y',
                color='red',
                labelcolor='blue',
                labelsize='xx-large')


# #### We can also get rid of the ticks and tick labels
# Here we modify the X axis:
# * <b>bottom=false</b> gets rid of the ticks
# * <b>labelbottom=false</b> removes the labels

# In[9]:


plt.tick_params(axis = 'x',
                bottom=False,
                labelbottom=False)


# #### Generate the sine wave and label the axes

# In[10]:


plt.plot(x, np.sin(x))

plt.xlabel('x', fontsize=15, color='green')
plt.ylabel('sin(x)', fontsize=15, color='green')


# #### Add a legend to the plot

# In[11]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()


# #### Set a title for the plot

# In[12]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()

plt.title('Playing with Plots')


# #### Setting limits on the axes
# xlim() and ylim() will set the range of values of the plot which will be visible in the plotted figure
# 
# This is effectively zooming into a portion of the plot

# In[13]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()
plt.title('Playing with Plots')

plt.xlim(1,5)


# #### Setting a ylim

# In[14]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()
plt.title('Playing with Plots')

plt.xlim(1,5)
plt.ylim(-1,0.5)


# #### Inverting the axes
# We invert the X axis to effectively create a mirror image along a vertical line

# In[15]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()
plt.title('Playing with Plots')

plt.xlim(5,1)
plt.ylim(-1,0.5)


# #### Inverting the Y axis as well

# In[16]:


plt.plot(x, np.sin(x), label='sine curve')

plt.legend()
plt.title('Playing with Plots')

plt.xlim(5,1)
plt.ylim(0.5, -1)


# In[ ]:





# In[ ]:





# In[ ]:




