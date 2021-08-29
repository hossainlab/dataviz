#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# ### Obtain dataset
# The dataset has been compiled from data obtained from here: https://irma.nps.gov/Stats/Reports/Park/GRCA
# 
# This shows the number of visits to the Grand Canyon National Park in each month from Jan-2011 to Dec-2017

# In[3]:


grand_canyon_data = pd.read_csv('datasets/grand_canyon_visits.csv')
grand_canyon_data.head()


# #### Examine the NumVisits data

# In[4]:


grand_canyon_data['NumVisits'].describe()


# #### Divide the NumVisits value by 1000
# When using the data for autocorrelation, large numbers may result in an overflow. To avoid this, we divide the NumVisits values by 1000

# In[5]:


grand_canyon_data['NumVisits'] = grand_canyon_data['NumVisits']/1000
grand_canyon_data['NumVisits'].describe()


# #### Plot the autocorrelation graph
# We set the maxlags attribute to 20 so that the series is compared with lags ranging from -20 to +20. Notice that the autocorrelation is highest when the lag is 12 in either direction, showing the seasonality of park visits. 

# In[6]:


plt.figure(figsize=(16,8))

plt.acorr(grand_canyon_data['NumVisits'], 
          maxlags=20)

plt.show()


# ### Components of the Autocorrelation plot
# * <b>lags:</b> List for each lag value in the autocorrelation plot. -20 to +20 in our example
# * <b>c:</b> The list containing the correlation values for each of the lag values
# * <b>vlines:</b> A collection of lines representing the vertical line for each lag value
# * <b>hline:</b> The Line2D object representing the horizontal line at 0

# In[15]:


plt.figure(figsize=(16,8))

lags, c, vlines, hline = plt.acorr(grand_canyon_data['NumVisits'], 
                             maxlags=20)

print('lags: ', lags, '\n')
print('c: ', c, '\n')
print('vlines: ', vlines, '\n')
print('hline: ', hline, '\n')


# In[ ]:




