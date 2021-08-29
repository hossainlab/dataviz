#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Use data about annual visits to some US national parks 
# Data obtained from: https://irma.nps.gov/Stats/Reports/Park
# 
# Number of annual visits in 3 US National parks from 1961-2017

# In[2]:


np_data= pd.read_csv('datasets/national_parks.csv')
np_data.head()


# In[3]:


np_data.describe()


# ### Histogram
# A histogram take in a series of data and divides the data into a number of bins. It then plots the frequency data points in each bin

# #### Plot a histogram for the number of annual visits to Grand Canyon National Park
# * The number of visits ranges from about 1.25M to 6.25M
# * Around 4.5M seems to be the most common number of annual visitors
# * We created 10 bins of data

# In[4]:


plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10)

plt.show()


# ### Components of a histogram
# The components of a matplotlib histogram are 3 lists:
# * <b>n:</b> Contains the frequency of each bin
# * <b>bins:</b> Represents the middle value of each bin
# * <b>patches:</b> The Patch object for the rectangle shape representing each bar

# In[5]:


n, bins, patches = plt.hist(np_data['GrandCanyon'], 
                            facecolor='cyan', 
                            edgecolor='blue', 
                            bins=10)

print('n: ', n)
print('bins: ', bins)
print('patches: ', patches)


# #### Set the bin values to probability densities
# p(x)δx  is the probability of measuring X in [x,x+δx]. With
# * p(x):= probability density.
# * δx:= interval length.
# 
# E.g. In our histogram the largest bin contains 16 of the 57 data points (28%). The interval for the histogram is about 5M (6.25M - 1.25M) and there are 10 bins, so about 500,000 for each bin. 
# 
# When converted to probability densities, the value of the largest bin is 5.6e-7. The probability for that bin is 500000*5.6e-7 = 0.28 

# In[7]:


n, bins, patches = plt.hist(np_data['GrandCanyon'], 
                            facecolor='cyan', 
                            edgecolor='blue', 
                            bins=10,
                            density=True)

print('n: ', n)
print('bins: ', bins)
print('patches: ', patches)


# #### The cumulative property
# If True, then a histogram is computed where each bin gives the counts in that bin plus all bins for smaller values. The last bin gives the total number of datapoints.

# In[8]:


plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10,
         cumulative=True)

plt.show()


# #### Restrict the histogram to a range of values
# We only look at the data points within the range 2M-5M. This realigns the bins in the histogram

# In[9]:


plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10,
         range=(2000000, 5000000))

plt.show()


# #### Overlay histograms
# We can add one more histogram to our plot - this park visits to Bryce Canyon National Park. This has fewer visitors and the number of visitors falls into a smaller range. Thus even with fewer bins each bin is narrower than the ones for Grand Canyon.<br />
# Notice that the histogram for Bryce Canyon obscures the one for Grand Canyon as it was added afterwards.

# In[10]:


plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10)

plt.hist(np_data['BryceCanyon'], 
         facecolor='lightyellow', 
         edgecolor='maroon', 
         bins=8)

plt.show()


# #### Swap the order of the histograms
# This time the Grand Canyon histogram obscures the one for Bryce Canyon

# In[11]:


plt.hist(np_data['BryceCanyon'], 
         facecolor='lightyellow', 
         edgecolor='maroon', 
         bins=8)

plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10)

plt.show()


# #### Adjust the alpha of the histograms to prevent obstruction

# In[12]:


plt.hist(np_data['BryceCanyon'], 
         facecolor='lightyellow', 
         edgecolor='maroon', 
         bins=8)

plt.hist(np_data['GrandCanyon'], 
         facecolor='cyan', 
         edgecolor='blue', 
         bins=10, 
         alpha = 0.3)

plt.show()


# In[ ]:




