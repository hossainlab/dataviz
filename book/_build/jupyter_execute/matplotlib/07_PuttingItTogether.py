#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# ### Dataset
# This contains the closing price of 10 stocks on the first trading day of each month from Jan 2007 to Jan 2017.
# 
# Data obtained from finance.yahoo.com

# In[2]:


stock_data = pd.read_csv('datasets/stocks.csv')
stock_data.head()


# #### Convert the Date field to datetime format
# This makes it easier to use the values in a plot

# In[3]:


stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.head()


# #### Draw two axes
# One axis is for the main data, the other is for reference. We set the coordinates to try to prevent the second axis from obscuring the line on thefirst axis

# In[4]:


fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])


# #### Draw the lines for two of the stocks
# Here, we examine AAPL close prices and compare to IBM during the same period

# In[5]:


fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])

ax1.plot(stock_data['Date'],
         stock_data['AAPL'],
         color='green')

ax1.set_title('AAPL vs IBM (inset)')


# In[6]:


fig = plt.figure(figsize=(10,6))

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])

ax1.plot(stock_data['Date'],
         stock_data['AAPL'],
         color='green')

ax1.set_title('AAPL vs IBM (inset)')

ax2.plot(stock_data['Date'],
         stock_data['IBM'], 
         color='blue')


# #### Compare multiple stocks
# We use multiple subplots in our figure in order to compare the stock prices of 4 stocks during this 10 year period.
# 
# Here we also specify a title for the figure

# In[8]:


fig = plt.figure(figsize=(10,6))

fig.suptitle('Stock price comparison 2007-2017', 
             fontsize=20)

ax1 = fig.add_subplot(221)

ax1.set_title('MSFT')

ax1.plot(stock_data['Date'],
         stock_data['MSFT'], 
         color='green')


# In[9]:


fig = plt.figure(figsize=(10,6))

fig.suptitle('Stock price comparison 2007-2017', 
             fontsize=20)

ax1 = fig.add_subplot(221)

ax1.set_title('MSFT')

ax1.plot(stock_data['Date'],
         stock_data['MSFT'], 
         color='green')

ax2 = fig.add_subplot(222)
ax2.set_title('GOOG')

ax2.plot(stock_data['Date'],
         stock_data['GOOG'], 
         color='purple')


# In[10]:


fig = plt.figure(figsize=(10,6))

fig.suptitle('Stock price comparison 2007-2017', 
             fontsize=20)

ax1 = fig.add_subplot(221)

ax1.set_title('MSFT')

ax1.plot(stock_data['Date'],
         stock_data['MSFT'], 
         color='green')

ax2 = fig.add_subplot(222)
ax2.set_title('GOOG')

ax2.plot(stock_data['Date'],
         stock_data['GOOG'], 
         color='purple')

ax3 = fig.add_subplot(223)
ax3.set_title('SBUX')

ax3.plot(stock_data['Date'],
         stock_data['SBUX'], 
         color='magenta')


# In[11]:


fig = plt.figure(figsize=(10,6))

fig.suptitle('Stock price comparison 2007-2017', 
             fontsize=20)

ax1 = fig.add_subplot(221)

ax1.set_title('MSFT')

ax1.plot(stock_data['Date'],
         stock_data['MSFT'], 
         color='green')

ax2 = fig.add_subplot(222)
ax2.set_title('GOOG')

ax2.plot(stock_data['Date'],
         stock_data['GOOG'], 
         color='purple')

ax3 = fig.add_subplot(223)
ax3.set_title('SBUX')

ax3.plot(stock_data['Date'],
         stock_data['SBUX'], 
         color='magenta')

ax4 = fig.add_subplot(224)
ax4.set_title('CVX')

ax4.plot(stock_data['Date'],
         stock_data['CVX'], 
         color='orange')


# In[ ]:




