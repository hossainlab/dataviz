#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# In[2]:


import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

from datetime import datetime


# ### Candlestick with pandas on Ford Motors stock
# A candlestick chart (also called Japanese candlestick chart) is a style of financial chart used to describe price movements of a security, derivative, or currency.

# #### Gather stock data
# First collect a few days of OHLC (Open High Low Close) data for the General Motors stock from Morningstar.

# In[3]:


ford = web.DataReader('F', 'morningstar',
                        
                    datetime(2018, 5, 1),
                    datetime(2018, 5, 10)).reset_index()


# #### Define the candlestick graph
# The fields which are passed to the chart include the OHLC fields along with the series which is represented on the X axis (typically the date)

# In[4]:


trace = go.Candlestick(x = ford.Date,
                       
                       open = ford.Open,
                       
                       high = ford.High,
                       
                       low = ford.Low,
                       
                       close = ford.Close)


# #### Plot the candlesticks
# The plot has the following components:
# * A bounding box whose y values represent the range between the stock's open and close prices 
# * A green box represents a higher close value than open (i.e. stock price went up that day)
# * The box is red when the stock closed lower
# * The vertical lines (bars above and below the box) show the range of intra-day high and low prices
# * The vertical lines are capped at the top by horizontal lines called whiserks. By default, the width of the whisker is 0 which is why we don't see them
# 
# Notice that a slider appears by default along the X axis

# In[5]:


data = [trace]

offline.iplot(data)


# ### Customizing the candlesticks
# The following customizations can be added to candlesticks:
# * Format the fillcolor of the bounding boxes which come in two forms:
#  * increasing represents the boxes when close > open (a green shade by default)
#  * decreasing represents the boxes when close < open (a red shade by default)
# * Format the lines of the bounding boxes and whiskers
# * Set the whisker width (as a proportion of box size. Default is 0, max is 1 which is equal to box size)

# In[15]:


trace = go.Candlestick(x = ford.Date,
                       open = ford.Open,
                       high = ford.High,
                       low = ford.Low,
                       close = ford.Close, 
                       
                       increasing = dict(fillcolor = 'greenyellow', 
                                         line = dict(color = 'green', 
                                                     width = 3
                                                    )
                                        ),
                       decreasing = dict(fillcolor = 'lightcoral'),
                       
                       whiskerwidth = 0.2
                      )


# In[16]:


data = [trace]


# In[17]:


fig = dict(data=data)

offline.iplot(fig)


# In[ ]:





# In[ ]:




