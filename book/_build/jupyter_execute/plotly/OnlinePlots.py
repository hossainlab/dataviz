#!/usr/bin/env python
# coding: utf-8

# ### Online Plots
# Plotly allows you to store your plots online in their cloud and share them with others. For this you need a Plotly account. Once the account is created, retrieve the API key which is required to link your Python code with your Plotly account so that your charts can be uploaded.

# #### plotly.plotly will be used to generate plots which get uploaded to your Plotly account

# In[1]:


import plotly
import plotly.plotly as py


# #### Set Plotly to use link up with your Plotly account
# You'll need your username and API key for this

# In[2]:


plotly.tools.set_credentials_file(username='yukti', api_key='0hlpfWI01Q4Ai07q5j8s')


# #### Plotting the chart
# Using plotly.plotly.iplot() will render the chart in the Jupyter notebook an also upload it to your Plotly account. Login to your plotly account and view the chart there and check out the options available for your plot.  

# In[3]:


py.iplot([{'x': [1, 3, 6], 
           'y': [3, 1, 5]}])


# #### Offline mode will be used for the remainder of this course
# This is for simplicity purposes. Uploading charts to your account makes it easier to share them, but this is not required for this course.

# In[ ]:




