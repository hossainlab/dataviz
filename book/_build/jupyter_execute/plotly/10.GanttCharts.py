#!/usr/bin/env python
# coding: utf-8

# # A Gantt chart provides a graphical illustration of a schedule that helps to plan, coordinate, and track specific tasks in a project.

# In[1]:


import plotly.plotly as py
import plotly.offline as offline

offline.init_notebook_mode(connected=True)


# #### Import Plotly's figure factory
# This is the package which contains the Gantt chart

# In[2]:


import plotly.figure_factory as ff


# #### Define a simple schedule
# The fields which are required to plot a Gantt Chart are:
# * <b>Task</b>, which is a string
# * <b>Start</b> which is the task's start time expressed in some date format
# * <b>Finish</b> which is the end time for the task, also in some date format
# 
# Note that the times for the tasks can overlap

# In[3]:


tasks = [dict(Task='Task 1', 
              Start='2018-01-01', 
              Finish='2018-02-28'),
         
         dict(Task='Task 2', 
              Start='2018-03-05', 
              Finish='2018-05-15'),
         
         dict(Task='Task 3', 
              Start='2018-05-01', 
              Finish='2018-06-30')]


# #### Plot the Gantt chart
# Use the figure factory to generate a Gantt Chart figure with our list of tasks

# In[4]:


fig = ff.create_gantt(tasks)

offline.iplot(fig)


# ### Using Color Scales
# Color scales can be used in Gantt charts to represent information

# ### Numeric data represented with a color scale
# By using a color scale, we can portray how much of a task is completed

# In[5]:


tasks = [dict(Task='Task 1', 
              Start='2018-01-01', 
              Finish='2018-02-28',
              Complete=100),
         
         dict(Task='Task 2', 
              Start='2018-03-05', 
              Finish='2018-04-15',
              Complete=60),
         
         dict(Task='Task 3', 
              Start='2018-04-15', 
              Finish='2018-06-30',
              Complete=20)]


# #### Define the Gantt chart
# * The <b>colors</b> attribute takes in the name of a built-in color scale or a list of RGB or Hexademical numbers
# * <b>index_col</b> is used to specify which field should be represented using the color scale
# * <b>show_colorbar</b> can be set to view the color scale as a reference 

# In[6]:


fig = ff.create_gantt(tasks, 
                      title = 'Gantt Chart with a color scale',
                      
                      colors = 'Picnic', 
                      index_col = 'Complete', 
                      show_colorbar = True)

offline.iplot(fig)


# ### Color Scales to represent string categories

# #### Import a CSV file containing a schedule
# The following is a schedule for a school going kid depicting his/her activities for 1-July-2018 

# In[7]:


import pandas as pd

schedule = pd.read_csv('./datasets/schedule.csv')
schedule


# #### Define a color map
# This needs to contain colors specified in either RGB or Hexadecimal format (named colors will not work in a Gantt Chart). The list can contain a mix of both RGB and Hex colors.
# 
# Here, we map the Category names to the color we want it to be portrayed by.

# In[8]:


color_dict = dict(Rest = 'rgb(46, 137, 205)',
                  Eat = 'rgb(114, 44, 121)',
                  Homework = 'rgb(198, 47, 105)',
                  
                  Play = '#BD8FD7',
                  Music = '#78F7DE')


# #### Draw the Gantt Chart
# We cannot use a named color scale to map String values, so we pass in our colors dictionary to be used to assign colors to the different values of 'Category' in our dataset.
# 
# <b>bar_width</b> sets the width (in this portrayal, the height) of each bar. A bar_width of 0.5 equals the distance between two grid lines on the Y axis. 

# In[9]:


fig = ff.create_gantt(schedule,
                      title='Schedule for 1-July-2018',
                      
                      colors=color_dict, 
                      index_col='Category',
                      show_colorbar=True,
                      
                      bar_width=0.5,
                      
                      showgrid_x=True, 
                      showgrid_y=True)

offline.iplot(fig)


# #### Alternatively, we use a color list
# Here, the ordering of colors will be mapped to the list of categories in alphabetical order.

# In[10]:


color_list = ['#BD8FD7', 
              '#78F7DE', 
              'rgb(198, 47, 105)', 
              'rgb(114, 44, 121)', 
              'rgb(46, 137, 205)']


# In[11]:


fig = ff.create_gantt(schedule,
                      title='Schedule for 1-July-2018',
                      
                      colors=color_list, 
                      index_col='Category',
                      show_colorbar=True,
                      
                      bar_width=0.5, 
                      showgrid_x=True, 
                      showgrid_y=True)

offline.iplot(fig)


# #### Grouping tasks
# In our schedule, there are 3 occurences of Music which have so far appeared as separate tasks. We use the group_tasks attribute so that they all appear in the same row on our plot.

# In[12]:


fig = ff.create_gantt(schedule,
                      title='Schedule for 1-July-2018',
                      
                      colors=color_list, 
                      index_col='Category',
                      show_colorbar=True,
                      
                      bar_width=0.5, 
                      showgrid_x=True, 
                      showgrid_y=True,
                      
                      group_tasks=True)

offline.iplot(fig)


# In[ ]:




