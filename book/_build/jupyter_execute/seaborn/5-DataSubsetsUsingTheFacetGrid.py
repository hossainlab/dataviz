#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# You have recently joined a startup as a social media manager. From the reports you see, the posts on facebook are not garnering as much of a response as those on twitter or instagram. Why is it so?
# You decide to study the kind of posts being made, analyse the response and see what is not working for the posts. Below is the dataset you receive from the team members.

# In[2]:


fb_data=pd.read_csv('datasets/dataset_Facebook.csv',
                     sep=r'\s*;\s*', engine='python')


# *The dataset discusses response on facebook for a set of posts that include different types/catogories.*

# In[3]:


fb_data.head()


# In[4]:


fb_data.describe()


# You decide to do some statistical analysis and plot them on graphs to visualise the status of the responses on facebook. Graphs are anyday easier to comprehend than a long list of numbers!

# Earlier, we tried to combine plots to simultaneously study relationships between pairs of variables - by exploiting the row, column and hue parameters along with lmplot and factorplot, for instance.
# Here, let us try to use the exclusive FacetGrid class that comes along with Seaborn. <br>
# 
# FacetGrid is a subplot grid for plotting conditional relationships.
# 
# FacetGrid is very useful for
# * Visualising distributions and relations between variables, within subsets of the concerned dataset.
# * As seen before, there are three dimensions along which we observe the data - row, column and hue.

# #### How do we use FacetGrid?
# * We first initialise a FacetGrid object with a dataframe
# * Specify the row, column and hue parameters
# * Every unique value of the categorical variable is then used to create a facet along the specified axis.
# * A plotting function is applied to each subset by using a map function
# 

# Let us create a FacetGrid object.

# In[5]:


g=sns.FacetGrid(fb_data, col="Type")


# We see that the matplotlib figure and axes are set up. We now have to map this with a plotting function, which will then be plotted on the above created structure. We will soon see that we can call different plots we have seen so far, alongwith the FacetGrid.

# In[6]:


g=sns.FacetGrid(fb_data, col="Type")
g.map(plt.hist, "Total Interactions")


# In[7]:


g=sns.FacetGrid(fb_data,col="Type")
g.map(plt.hist,"Total Interactions")

plt.xlim(-20,3000)
plt.ylim(0,30)


# We have called the plt.hist function to plot a histogram for the total interactions for the different types of posts made on facebook.
# 
# It is clear that the post containing a photograph is the biggest winner. It has the maximum interaction in the form of comments, likes and shares. The histogram shows that the interaction between 0 and 500 has the largest area, implying highest number of interactions.
# 
# All posts have more interactions in the range of 50 to 500. 
# 
# The posts with a status are more popular than those with links or videos.

# #### We now pass multiple variables to make a relational plot.
# The scatter plot is used

# In[11]:


g=sns.FacetGrid(fb_data, col="Type")
g.map(plt.scatter,"Lifetime Post Total Reach", "Lifetime Engaged Users")


# #### Adding a legend to show what the colors stand for
# We have added "alpha=0.7" to reduce the opacity of the points in the scatterplot. 
# It is 1 by default. Making it closer to 0 makes it more transparent.

# In[12]:


g=sns.FacetGrid(fb_data,col="Type",hue="Paid")

g.map(plt.scatter,"Lifetime Post Total Reach","Lifetime Engaged Users", alpha=0.7)

g.add_legend()


# We can see that there are more posts that reach just less than about 50000 people. From the graph, we see that paid posts seem to be able to engage users for lifetime, while both paid and unpaid posts in this dataset seem to have the same reach.

# Calling the reg plot(), 
# 
# * The margin title parameter is made true to add the title for each row
# * fit_reg is made false as we do not want to plot a regression line

# In[14]:


g=sns.FacetGrid(fb_data, row="Category", col="Type", hue="Paid", margin_titles=True)

g.map(sns.regplot,"Post Month", "Total Interactions", fit_reg=False)

g.add_legend()
plt.ylim(0,2500)


# The above shows different kinds of facebook posts made throughout the year, and the total interactions received from all posts.
# * The patterns show that paid posts made in the second half of the year have more interactions.
# * Unpaid posts hit a high response at the start and end of the year for photos, mid year for status posts and end of the year for video posts. Links seem to have a mediocre standard response throughout the year.
# * Category 1 posts have the best response for photos, while category 2 favours posts with statuses most.

# ### In the above plot, we have more details in the 1st plot when compared to the other two. Can we create plots such that each individual plot has a different size?
# Yes, we use the gridspec parameter.

# In[16]:


g=sns.FacetGrid(fb_data,row="Category", col="Type",hue="Paid", margin_titles=True,
                gridspec_kws={"width_ratios":[5, 3, 2, 2]})

g.map(sns.regplot,"Post Month","Total Interactions",fit_reg=False)

g.add_legend()
plt.ylim(0,2500)


# ### What if we want to specify colours that the graph has to use for each parameter?
# *Create a dictionary with key as parameter and value as the color, for the hue variable*

# In[17]:


h={0:"red",1:"green"}
g=sns.FacetGrid(fb_data,row="Category", col="Type",hue="Paid", margin_titles=True,
                palette=h)

g.map(sns.regplot,"Post Month","Total Interactions",fit_reg=False)

g.add_legend()
plt.ylim(0,2500)


# ### Can we extend the same to other aspects of the hue variable?
# Pass the arguments in exactly the same manner as above to hue_kw parameter

# In[18]:


#Creating a dictionary for markers and passing it to hue_kws variable
h={0:"red",1:"green"}
i={"marker":["^","v"]}

g=sns.FacetGrid(fb_data,row="Category", 
                col="Type",
                hue="Paid", 
                margin_titles=True,
                palette=h,
                hue_kws=i)


g.map(sns.regplot,"Post Month","Total Interactions",fit_reg=False)

g.add_legend()
plt.ylim(0,2500)


# *We see that the points are plotted with the specified markers. As we have also specified colours, we see that the markers are in accordance with the passed in color scheme*

# In[ ]:





# Calling the bar plot,

# In[21]:


g=sns.FacetGrid(fb_data, col="Type")

g.map(sns.barplot, "Post Weekday", "Page total likes")


# We can see that
# * The number of likes received for photos are equal for every day of the week
# * Likes for status posts dropped midweek
# * The likes for posts with links increased slowly with every day of the week. Friday saw the most number of likes
# * Likes for videos posted was almost constant throughout, slowly increasing in number as weekend emerged

# ### In the above plot, what if we want to print the video data first, followed by photos, status and then links?
# *We simply pass in an ordered list to the corresponding parameter, for eg, row_order, hue_order, etc.* <br>
# By default, the variables are ordered in ascending order if they are numbers, and in the order of appearance otherwise.

# In[20]:


g=sns.FacetGrid(fb_data,col="Type", col_order=["Video", "Photo", "Status", "Link"])

g.map(sns.barplot,"Post Weekday","Page total likes")


# In[ ]:





# Let us plot the same graph for every month now. We will know the how the number of likes overall varies every month.

# In[22]:


g=sns.FacetGrid(fb_data, col="Post Month")
g.map(sns.barplot,"Post Weekday", "Page total likes")


# ### We have to zoom in into each graph if we want to understand this. Do we have a way to make them of readable size and position them better?

# In[23]:


g=sns.FacetGrid(fb_data, col="Post Month", col_wrap=4)
g.map(sns.barplot,"Post Weekday", "Page total likes")


# Posts seem to be better received in the last quarter of the year.
# 
# We have added the col_wrap parameter and set it to 4. Thus we have 4 columns in every row, and the rest of the entries are carried forward to the next rows. <br>
# **Note: The same cannot be applied to the row variable**

# In[ ]:




