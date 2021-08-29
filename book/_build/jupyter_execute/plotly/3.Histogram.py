#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Create a list of 200 random numbers

# In[2]:


random_numbers = np.random.randn(200)


# #### Produce a histogram to plot the distribution of these numbers
# We assign this list to the axis on which we want the bars to be placed. The frequency will be displayed on the other axis. 

# In[3]:


hist = go.Histogram(x = random_numbers)


# #### Generate the histogram plot

# In[4]:


data = [hist]

offline.iplot(data)


# #### Normalized Histogram
# Rather than raw numbers, this will display the probability of the occurence of a value in a bin. The shape will be exactly the same as the previous histogram, but the Y axis will denote the probability rather than the raw frequency.

# In[5]:


hist = go.Histogram(x = random_numbers,
                     histnorm = 'probability'
                    )


# In[6]:


data = [hist]

offline.iplot(data)


# #### Plotting a cumulative histogram
# In such a histogram, a bin gives not just the counts for a single bin, but rather gives the counts for that bin plus all bins for smaller values of the response variable.

# In[7]:


hist = go.Histogram(x = random_numbers,
                    
                    cumulative = dict(enabled=True)
                    )


# In[8]:


data = [hist]

offline.iplot(data)


# #### Horizontal Histogram
# A histogram can also be oriented horizontally. This is done by merely flipping the axis along which the bins should be rooted.

# In[9]:


hist = go.Histogram(y = random_numbers)


# In[10]:


data = [hist]

offline.iplot(data)


# ### Overlaid Histogram
# We can plot histograms for multiple variables in a single plot. One way to view multiple histograms is to overlay them.
# 
# To start off, we create another series of data which we will use along with the previous one. This one has fewer elements and we generate an offset of 1 so that the bins of this series does not fully overlap with those of the previous series.

# In[11]:


more_random_numbers = 1 + np.random.randn(100)


# #### Our first histogram
# This one uses the first random_number series. We set an opacity level for the histogram plot.

# In[12]:


trace0 = go.Histogram(x = random_numbers, 
                      opacity=0.9
                     )


# #### The second histogram
# THis uses the newly created series, and has a lower opacity.

# In[13]:


trace1 = go.Histogram(x = more_random_numbers, 
                      opacity=0.5
                     )


# #### Set the data and layout for the plot
# In the layout, we specify the barmode attribute to be 'overlay'

# In[14]:


data = [trace0, trace1]

layout = go.Layout(barmode = 'overlay')


# #### Plot the histograms

# In[15]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# #### Stacked histograms
# If wish to the combined distribution of two series, we can stack their histograms. For that we set the barmode to 'stack'.

# In[16]:


layout = go.Layout(barmode = 'stack')


# In[17]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# ### Styled Histogram
# We can apply a number of styling properties to histograms. We explore some of them here.

# #### Define the first histogram in our plot
# * xbins: start and end set the range for the entire histogram plot. Size sets the width of each bin
# * marker: this is used to configure the histogram bins

# In[18]:


trace0 = go.Histogram(x = random_numbers,
                      
                      name = 'Series 1',
                      
                      xbins = dict(start = -4,
                                   end = 4,
                                   size = 0.5
                                  ),
                      
                      marker = dict(color = '#D67D93'),
                      
                      opacity = 0.75
                     )


# #### Define the second histogram
# We use the same bin size as the previous histogram to make it easier for comparison. However, it is not required to have the same bin size - but the histogram bars will be unevenly spaced in the plot

# In[19]:


trace1 = go.Histogram(x = more_random_numbers,
                      
                      name = 'Series 2',
                      
                      xbins = dict(start = 0,
                                   end = 4,
                                   size = 0.5
                                  ),
                      
                      marker = dict(color = '#7DAED6'),
                      
                      opacity = 0.75
                     )


# In[20]:


data = [trace0, trace1]


# #### Define the layout
# * bargap sets the distance (in plot units) between bars of adjacent location coordinates (i.e. adjacent x value here)
# * bargroupgap sets the distance between bars in the same group (i.e. same x value)

# In[21]:


layout = go.Layout(title='Styled histograms',
                   
                   xaxis=dict(title='Value'),
                   yaxis=dict(title='Count'),
                   
                   bargap=0.2,
                   
                   bargroupgap=0.1
)


# In[22]:


fig = go.Figure(data=data, 
                layout=layout)

offline.iplot(fig)


# 
