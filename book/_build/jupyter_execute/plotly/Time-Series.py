#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Install Pandas Data Reader
# Pandas Data Reader is a tool to download data from a variety of remote sources into a Pandas dataframe. The list of remote sources currently supported can be found here: <br />
# http://pandas-datareader.readthedocs.io/en/latest/remote_data.html
# 
# A number of data sources are supported, including Google Finance, IEX, World Bank etc. 

# Functions from pandas_datareader.data and pandas_datareader.wb extract data from various Internet
# sources into a pandas DataFrame. Currently the following sources are supported:
# • Google Finance
# • Morningstar
# • IEX
# • Robinhood
# • Enigma
# • Quandl
# • St.Louis FED (FRED)
# • Kenneth French’s data library
# • World Bank
# • OECD
# • Eurostat
# • Thrift Savings Plan
# • Nasdaq Trader symbol definitions
# • Stooq
# • MOEX

# In[2]:


get_ipython().system('pip install pandas_datareader --upgrade')


# In[3]:


from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web


# #### Get Amazon stock data from Morningstar
# Morningstar is an investment research and management firm which supplies OHLC (Open, High, Low, Close) data for stocks. We get the OHLC data for Amazon stock for an 18-month period from 1-Jan-2017 to 1-Jun-2018.

# In[21]:


amzn = web.DataReader('AMZN', 'morningstar',
                      
                      datetime(2017, 1, 1),
                      datetime(2018, 6, 1)).reset_index()

amzn.head()


# #### Plot a graph of high price vs date
# This will produce a time series

# In[22]:


data = [go.Scatter(x=amzn.Date, 
                   y=amzn.High)]

offline.iplot(data)


# #### Plot Amazon high and low on the same graph

# In[6]:


trace_high = go.Scatter(x=amzn.Date,
                        y=amzn.High,
                        
                        name = "Amazon High",
                        
                        line = dict(color = '#6699FF')
                       )


# In[7]:


trace_low = go.Scatter(x=amzn.Date,
                       y=amzn.Low,
                       
                       name = "Amazon Low",
                       
                       line = dict(color = '#FF6633')
                      )


# In[8]:


data = [trace_high, trace_low]

layout = dict(title = "Amazon Stock Price Data ")


# In[9]:


fig = dict(data=data, 
           layout=layout)

offline.iplot(fig)


# ### Range slider
# We can add a range slider to an axis to allow the range of data displayed to be restricted

# In[27]:


layout = dict(title = 'Amazon Stock Price Data',
              
              xaxis = dict(rangeslider=dict(),
                           type='date')
             )


# In[28]:


fig = dict(data=data, 
           layout=layout)

offline.iplot(fig)


# #### Range Selector
# In addition to range sliders, we can include rangeselector buttons where we can quickly restrict the plotted range:
# * <b>step</b> is a time interval to set the range. Can be year, month, day, hour, minute, second and all
# * <b>stepmode</b> value can be 'todate' or 'backward'. 
#  * A value of 'todate' with a step of 'month' means that the left of the range slider will move to the start of the month (and the right will remain where it is)
#  * A value of 'backward' will keep the right slider where it is, and shift the left slider back by the value of count. In our example, the left slider will move back 6 months from the position of the right slider

# In[42]:


layout = dict(
    
    title = 'Amazon Stock Price Data ',
    
    xaxis = dict(rangeselector = dict(buttons = list([dict(count = 1,
                                                           label = '1m',
                                                           step = 'month',
                                                           stepmode = 'todate'),
                                                  
                                                      dict(count = 6,
                                                           label = '6m',
                                                           step = 'month',
                                                           stepmode = 'backward'),
                                                  
                                                      dict(step = 'all')])
                                     ),
                 
                 rangeslider=dict(),
                 type='date'
    )
)


# In[43]:


fig = dict(data=data, 
           layout=layout)

offline.iplot(fig)


# In[ ]:




