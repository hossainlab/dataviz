#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Create an array of integers for our boxplot

# In[2]:


x = np.random.randint(low=0, high=20, size=20)
x.sort()
x


# #### Create a boxplot
# * The box represents the data in the middle two quartiles of the range (25th percentile to 75th percentile)
# * The horizontal colorful line in the middle is the median
# * The lines outside the box (called whiskers) represent the range of values in the distribution - but not the outliers

# In[3]:


plt.boxplot(x)

plt.show()


# #### Appending a high value at the end to view the change in the boxplot
# The top whisker gets elongated to include the new data. The box and the median should also change slightly

# In[4]:


x = np.append(x, 22)

plt.boxplot(x) 

plt.show()


# #### Outliers are separate from the box and whiskers
# A circle will be used to denote outliers in the data

# In[5]:


x = np.append(x, 37)
x = np.append(x, 40)

plt.boxplot(x) 

plt.show()


# #### The boxplot can be oriented horizontally

# In[6]:


plt.boxplot(x, vert=False) 

plt.show()


# #### A notch can be added to the box around the median
# This is to make the median more prominent

# In[7]:


plt.boxplot(x, 
            vert=False,
            notch=True) 

plt.show()


# #### The outliers/fliers can be hidden from the boxplot
# Note that the values of the median, and the quartile ranges does not change - the outlier/flier values still affect those. Those fliers are just not visible in the plot

# In[8]:


plt.boxplot(x, 
            vert=False,
            notch=True,
            showfliers=False) 

plt.show()


# ### Formatting the boxplot

# #### Convert the box to a PathPatch object
# By default it is a Line2D object which limits formatting options. We convert to a PathPatch by setting the patch_artist of the boxplot to true. <br />
# Here, we also view all the components of a boxplot

# In[9]:


bp = plt.boxplot(x, patch_artist=True) 
bp


# #### View the number of each boxplot component
# There are two whiskers (lower and upper in that order), two caps(lower and upper in that order) and one of each other component. Even though the data has two outlier points, there is one object which represents them

# In[10]:


print('Number of boxes: ', len(bp['boxes']))
print('Number of whiskers: ', len(bp['whiskers']))
print('Number of caps: ', len(bp['caps']))
print('Number of medians: ', len(bp['medians']))
print('Number of fliers: ', len(bp['fliers']))


# #### We set the color of the box

# In[11]:


bp = plt.boxplot(x, patch_artist=True) 

bp['boxes'][0].set(facecolor='lightyellow', 
                   edgecolor='maroon', 
                   hatch='.')


# #### Define the whiskers
# Whisker #0 is the bottom one, #1 is above the box

# In[12]:


bp = plt.boxplot(x, patch_artist=True) 

bp['boxes'][0].set(facecolor='lightyellow', 
                   edgecolor='maroon', 
                   hatch='.')

bp['whiskers'][0].set(color='red', 
                      linewidth=2)

bp['whiskers'][1].set(color='blue')


# #### Define the caps
# Caps are the horizontal lines at the ends of the whiskers. Cap #0 is at the end of whisker #0 and whisker and cap #1 are also attached

# In[13]:


bp = plt.boxplot(x, patch_artist=True) 

bp['boxes'][0].set(facecolor='lightyellow', 
                   edgecolor='maroon', 
                   hatch='.')

bp['whiskers'][0].set(color='red', 
                      linewidth=2)

bp['whiskers'][1].set(color='blue')

bp['caps'][0].set(color='purple')

bp['caps'][1].set(color='pink',
                  linewidth=2)


# #### Define the outlier plots
# Outliers are termed "fliers" in boxplots. We can set the format for these as well

# In[15]:


bp = plt.boxplot(x, patch_artist=True) 

bp['boxes'][0].set(facecolor='lightyellow', 
                   edgecolor='maroon', 
                   hatch='/')

bp['fliers'][0].set(marker='D', 
                    markerfacecolor='blue')


# #### Define the median line

# In[18]:


bp = plt.boxplot(x, patch_artist=True) 

bp['boxes'][0].set(facecolor='lightyellow', 
                   edgecolor='maroon')

bp['medians'][0].set(linestyle='--', 
                     linewidth=3)


# ### Using boxplots with real data
# We load student scores in Math, Reading and Writing.<br /> 
# <b>Dataset source: </b>http://roycekimmons.com/system/generate_data.php?dataset=exams&n=100 

# #### Use Pandas to load the dataset

# In[19]:


import pandas as pd


# In[20]:


exam_data = pd.read_csv('datasets/exams.csv')


# In[21]:


exam_data.head()


# #### We only extract the exam scores
# We will then use the data in our boxplot

# In[22]:


exam_scores = exam_data[['math score', 'reading score', 'writing score']]
exam_scores.head()


# #### Examine the data
# This will give an idea of what our box plot will look like

# In[23]:


exam_scores.describe()


# #### To use the data in a boxplot, we convert it to an array
# Numpy is nice enough to eliminate the header row

# In[24]:


exam_scores_array = np.array(exam_scores)
exam_scores_array


# #### Draw the boxplot to represent the exam scores

# In[25]:


bp = plt.boxplot(exam_scores_array)

plt.show()


# #### Components of the boxplot
# The number of each component should be 3 times what we saw in when we only had one set of data

# In[28]:


bp = plt.boxplot(exam_scores_array, 
                 patch_artist=True)


# In[29]:


print('Number of boxes: ', len(bp['boxes']))
print('Number of whiskers: ', len(bp['whiskers']))
print('Number of caps: ', len(bp['caps']))
print('Number of medians: ', len(bp['medians']))
print('Number of fliers: ', len(bp['fliers']))


# ### Formatting this new boxplot

# #### The colors to use for the boxes

# In[30]:


colors = ['blue', 'grey', 'lawngreen']


# #### Set the formats
# We don't do much here - just set the facecolor for the box and the color for the top cap

# In[31]:


bp = plt.boxplot(exam_scores_array, 
                 patch_artist=True)

for i in range(len(bp['boxes'])):
    
    bp['boxes'][i].set(facecolor=colors[i])
    
    bp['caps'][2*i + 1].set(color=colors[i])


# #### We set the xtick value to portray what the box plots represent

# In[32]:


bp = plt.boxplot(exam_scores_array, 
                 patch_artist=True)

for i in range(len(bp['boxes'])):
    
    bp['boxes'][i].set(facecolor=colors[i])
    
    bp['caps'][2*i + 1].set(color=colors[i])
    
plt.xticks([1, 2, 3], ['Math', 'Reading', 'Writing'])


# ### Violin Plots
# These are similar to boxplots, except they can show the density of the data points around a particular value with their widths

# #### Exam score distribution
# This allows us to visualise how the scores are spread out in each course: <br />
# * Math and Writing scores are densest around 70
# * Reading scores have the highest density at arund 60 but density gets only marginally lower all the way up to 80. Density drops significantly below 60

# In[33]:


vp = plt.violinplot(exam_scores_array)
plt.show()


# #### Show median and xticks
# Use the showmedians parameter to display the median value on the plot (unlike boxplots, it's not visible by default). <br />
# Set the xticks just as we did in the boxplot

# In[34]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True)

plt.xticks([1, 2, 3], ['Math', 'Reading', 'Writing'])

plt.show()


# ### Formatting the violin plot

# #### We re-define the same plot, but oriented horizontally
# Note that we now set the yticks to display the subjects rather than xticks. <br />
# We also view the components of the violin plot

# In[39]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True,
                    vert=False)

plt.yticks([1, 2, 3], ['Math', 'Reading', 'Writing'])


# In[40]:


vp


# #### Not exactly the same as a Boxplot
# Only the "bodies" component is a list and can be compared to the "boxes" in a Boxplot

# In[37]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True,
                    vert=False)

plt.yticks([1, 2, 3], ['Math', 'Reading', 'Writing'])

for i in range(len(vp['bodies'])):
    
    vp['bodies'][i].set(facecolor=colors[i]) 


# #### The other Violinplot components
# Everything else is common for the entire plot - so we can't customize them individually for each violin (unlike in a Boxplot). We specify some formatting for each of these components which will apply to every violin

# In[42]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True,
                    vert=False)

plt.yticks([1, 2, 3], ['Math', 'Reading', 'Writing'])

for i in range(len(vp['bodies'])):
    vp['bodies'][i].set(facecolor=colors[i]) 
    
vp['cmaxes'].set(color='maroon')

vp['cmins'].set(color='black')

vp['cbars'].set(linestyle=':')

vp['cmedians'].set(linewidth=6)


# #### Add a legend to the plot
# When adding a legend we pass the following data: <br />
# * <b>handles:</b> These represent Artists(lines/patches) in the plot for which legends are needed (the colors for these are automatically picked up by Matplotlib). Here we only include 2 of the 3 Patches in the legend
# * <b>labels:</b> These are the labels for the corresponding handles
# * <b>loc:</b> This is the location of the legend - we use this in conjunction with the bbox_to_anchor
# * <b>bbox_to_anchor:</b> The axis coordinates (on a 1x1 scale where (1,1) is the top right of the axis) at which the legend will be anchored from the "loc". In our example, the "top left" of the legend will be anchored to position (1,1) i.e. the top right of the axis

# In[47]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True,
                    vert=False)

plt.yticks([1, 2, 3], ['Math', 'Reading', 'Writing'])

for i in range(len(vp['bodies'])):
    vp['bodies'][i].set(facecolor=colors[i]) 
    
plt.legend(handles = [vp['bodies'][0], vp['bodies'][1]],
           labels = ['Math', 'Reading'], 
           loc = 'upper left')


# In[48]:


vp = plt.violinplot(exam_scores_array,
                    showmedians=True,
                    vert=False)

plt.yticks([1, 2, 3], ['Math', 'Reading', 'Writing'])

for i in range(len(vp['bodies'])):
    vp['bodies'][i].set(facecolor=colors[i]) 
    
plt.legend(handles = [vp['bodies'][0], vp['bodies'][1]],
           labels = ['Math', 'Reading'], 
           loc = 'upper left',
           bbox_to_anchor = (1,1))


# In[ ]:




