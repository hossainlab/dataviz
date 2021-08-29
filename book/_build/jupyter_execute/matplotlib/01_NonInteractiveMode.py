#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


import matplotlib

print(matplotlib.__version__)


# #### Check whether Matplotlib is in interactive mode
# 
# https://matplotlib.org/faq/usage_faq.html#what-is-interactive-mode
# 
# The default settings may vary according to your system
# 
# * Non-interactive mode delays all drawing to screen till the plt.show() function is called, more efficient
# * Also in the interactive mode pyplot functions behave a little differently from matplotlib functions

# In[3]:


matplotlib.is_interactive()


# #### Run in non-interactive mode

# In[4]:


matplotlib.interactive(False)


# In[5]:


import matplotlib.pyplot as plt

plt.ioff()
matplotlib.is_interactive()


# #### Define a simple plot
# We use pyplot to plot a simple straight line.
# * The first argument is a list of x coordinates
# * The second argument is a list of y coordinates

# In[6]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16])


# #### plt.show() will render the plot

# In[7]:


plt.show()


# #### Switch to interactive mode

# In[8]:


matplotlib.interactive(True)


# #### This will result in the plot being rendered without having to run plt.show()
# Running in interactive mode can be useful when we are using interacive plots (covered in the next demo). But here, and for nearly all demos in this course, we will keep things simple and work with non-interactive plots.
# 
# When running in interactive mode to plot non-interactiveplots, **Matplotlib ends up plotting your figure and closing it after the execution of any cell which references your plot. The result is that the entire plot will need to be defined within one cell. **
# 
# In the upcoming demos (except the next one), when our plots get more and more complex, this will become a problem which is why we will run in non-interactive mode.

# In[9]:


plt.plot([2, 4, 6, 8], 
         [4, 8, 12, 16])


# In[ ]:




