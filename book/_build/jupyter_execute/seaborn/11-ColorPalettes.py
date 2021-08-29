#!/usr/bin/env python
# coding: utf-8

# # Color palettes: sequential, diverging and qualitative

# Why do you like to see patterns and graphs more than simply rows and columns of data? The patterns stand out, the colours speak loud and the effect is visually pleasing.
# 
# But what if all graphs are made simple and plain? What if instead of using colours for the bars in a barplot, we use it only the for labels and axes?
# 
# Colors in graphs are very important. If used the right way, they can enhance your plot a great deal, but if not paid attention to, they could hide very important details.
# 
# Seaborn provides the option to use colours for visualising data, through a variety of palettes.

# In[1]:


import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


fb_data=pd.read_csv('datasets/dataset_Facebook.csv',
                     sep=r'\s*;\s*', engine='python')


# The simplest way to choose colours in Seaborn is to call the color_palette() function.
# * Most helpful when working with discrete colors
# * You can pass in the name of any Seaborn palette, matplotlib colormap, list of colors specified in valid matplotlib formats (RGB tuples, hex color codes, HTML color names)
# * If the function is called without any arguments, the default color cycle is returned.
# * Combine this with a "with" function to temporarily set color to the plot
# * You can also set the same using the set_palette function. This will then be used as the default matplotlib parameters for all plots that follow.
# 
# *The last two points are demonstrated below*
# 
# 
# 

# In[6]:


sns.set_palette("Greens_d")

f, ax=plt.subplots(figsize=(10,5))

sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[7]:


sns.set_style("whitegrid")

with sns.color_palette("Blues"):
    
    f,ax=plt.subplots(figsize=(10,5))

    sns.distplot(fb_data['Lifetime Post Total Reach'])


# In[ ]:





# Depending on the kind of data you want to plot, you can choose from different categories of palettes:
# * Qualitative palettes for categorical data
# * Sequential or Diverging plots for large range of data 

# ## Qualitative Color Palettes

# These palettes are mostly useful for plots that have categorical data, or data that varies in discrete chunks without an inherent ordering. It comes with 6 variations of default themes.

# In[8]:


sns.set()


# Let us use the Seaborn function palplot() to plot the values in the color palette as a horizontal array

# In[9]:


current_palette=sns.color_palette()
sns.palplot(current_palette)


# The six variations are deep, muted, pastel, bright, dark and colorblind.

# #### What does this translate to in a graph??
# 
# Just to understand this, let us plot a graph that involves multiple lines of different colours. Invoking the kde plot with different bandwidths, as seen in module 1, we get the below:

# In[10]:


f,ax=plt.subplots(figsize=(15,5))

sns.set_context("poster") 
#This has been added just to see the colours better. We will look at this option in Module 3c.

sns.kdeplot(fb_data['Total Interactions'], bw=.04, label="bw: 0.04")
sns.kdeplot(fb_data['Total Interactions'], bw=1, label="bw: 1")
sns.kdeplot(fb_data['Total Interactions'], bw=2, label="bw: 2")
sns.kdeplot(fb_data['Total Interactions'], bw=5, label="bw: 5")
sns.kdeplot(fb_data['Total Interactions'], bw=7, label="bw: 7")
sns.kdeplot(fb_data['Total Interactions'], bw=9, label="bw: 9")

plt.xlim(-50,800)


# *We see that the plot above needs six different colours, which are the different shades in the default palette we saw above*

# In[ ]:





# ### What if there are more than 6 colours/lines needed in the plot?
# **Remember the graphs we plotted in Module 1d on the wine dataset. There were violin plots, hue based on pH; we saw a variety of colours there. How does Seaborn do this?**<br>
# 
# *It uses a circular color space where the hue changes based on overlap of colors.*

# In[11]:


sns.palplot(sns.color_palette("hls", 12))


# * Varying the brightness and intensity of those plots
# * Here, we are setting the lightness and saturation content of the hue.

# In[17]:


sns.palplot(sns.hls_palette(12, l=0.2, s=0.5))


# If we look at the strips above, it looks like the yellow-green range is brighter than the blue region. While this is not actually the case as all of these are of the same intensity in terms of RGB levels, our eyes perceive colours differently. 

# To have a plot with same intensity as per human perception, you could make use of:
# * husl interface 
#         - you can use this by calling the 'husl' word with the color_palette function
#         - you could also call it using the husl_palette() function
# * Categorical Color Brewer Palette
#         - Takes the help of the Color Brewer Tool
#         - Calling a Color Brewer palette gives distinct colours, which cycle
#         - Can use an ipython notebook to check the color brewer help catalogue

# How do we know what palettes are available? How can we know what are the different colour shades Seaborn will choose when we assign a certain palette to a plot?
# Seaborn offers an interface to the Color Brewer palette, and we can interactively see what Color Brew has to offer, as below.

# In[40]:


#Help for choosing a qualitative panel
sns.choose_colorbrewer_palette('qualitative')


# We see that the pairplot has pairs of colours that together form the color panel. Observe that the exact shades shown above are the ones used in the graph below.

# In[42]:


sns.pairplot(fb_data, 
             vars=["like", "share", "comment"],
             hue="Post Month",
             palette = "Paired")


# ### Can you specify colours explicitly?
# Method1: List out the hex codes

# In[20]:


sns.palplot(sns.color_palette(["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]))


# Method 2: Using named colors from the xkcd color survey that named RGB colors
# Lets plot curves with a specific color for each

# In[21]:


#setting the size for the plot
f,ax=plt.subplots(figsize=(15,5))

sns.xkcd_rgb["pale red"]
sns.kdeplot(fb_data['Total Interactions'], bw=.04, label="bw: 0.04")

sns.xkcd_rgb["medium green"]
sns.kdeplot(fb_data['Total Interactions'], bw=1, label="bw: 1")

sns.xkcd_rgb["denim blue"]
sns.kdeplot(fb_data['Total Interactions'], bw=2, label="bw: 2")


plt.xlim(-50,800)


# ## Sequential Color Palettes
# These palettes are most useful for plots where the data has a wide range, but the relatively low values are uninteresting, and the relatively high values are interesting.
# 
# * These are very commonly used as colormap in functions like kdeplot() or such matplotlib functions.
# * Best to use palettes that have a relatively subtle shift in hue, accompanied by a large shift in brightness and saturation. Important data is highlighted well.
# * You can choose the Color Brewer library for this too.

# In[22]:


#Using the Blues palette
sns.palplot(sns.color_palette("Blues"))


# In[23]:


#Reversing the lightness ramp in the palette
sns.palplot(sns.color_palette("Blues_r"))


# If you want to restrict the range of colors, to create a dark palette. This comes in handy while mapping lines or points for clarity.

# In[24]:


sns.palplot(sns.color_palette("Blues_d"))


# #### Custom sequential palettes
# Two functions - light_palette() and dark_palette() both have a single colour, with a range of intensities.

# In[25]:


sns.palplot(sns.light_palette("green"))


# Plotting a kdeplot with the above color palette. We use it as an object and pass it to the color map variable

# In[26]:


#setting the size for the plot
f,ax=plt.subplots(figsize=(10,5))

cmap = sns.light_palette("green", as_cmap=True, reverse=True)
sns.kdeplot(fb_data['Total Interactions'],fb_data['Lifetime Post Total Reach'], 
            cmap=cmap);
#We can set the n_levels parameter to specify number of hue levels we need

plt.xlim(-100,400)
plt.ylim(-5000,15000)


# In[27]:


sns.palplot(sns.dark_palette("purple", reverse=True))


# *A reversed dark palette is similar in intensities to a light palette*

# Note: Functions like choose_cubehelix_palette(), choose_light_palette(),choose_dark_palette() can be used to interactive widgets to create these palettes.

# In[43]:


#Interactively see the palettes available for sequential distributions of data
sns.choose_colorbrewer_palette('sequential')


# ##### Cubehelix Palettes
# This is a sequential palette with a linear increase or decrease in brightness, along with hue variation.
# *What is the advantage of this? Print the image, and even in the black and white image, the information will be preserved thanks to the variation in brightness.. It also works in favour of those with color blindness.*

# In[29]:


#Default cubehelix from matplotlib
sns.palplot(sns.color_palette("cubehelix", 12))


# In[30]:


#Calling the default cubehelixpalette in Seaborn,
sns.palplot(sns.cubehelix_palette(12))


# We make few observations about the default cubehelix pattern, when compared to the matplotlib version
# * The color range is smaller
# * The intensity range covered is lesser
# * The order of colors is reversed - important values are darker.
# 
# 
# Storing this object in a variable and mapping it in a kde plot,

# In[31]:


#setting the size for the plot
f,ax=plt.subplots(figsize=(10,5))

cmap = sns.cubehelix_palette(as_cmap=True, dark=1, light=0, reverse=True)
sns.kdeplot(fb_data['Total Interactions'],fb_data['Lifetime Post Total Reach'], 
            cmap=cmap, shade=True);
#We can set the n_levels parameter to specify number of hue levels we need

plt.xlim(-100,400)
plt.ylim(-5000,15000)


# **Customising the Cubehelix plot,**

# In[285]:


#Start between a value of 0 and 3; number of rotations between -1 and +1 on the hue wheel
sns.palplot(sns.cubehelix_palette(12, start=1, rot=-.70))


# In[286]:


#Control the brightness of the dark and light points, and reverse the map.
sns.palplot(sns.cubehelix_palette(12, start=1, rot=-.70, dark=0.55, light=0.95, reverse=True))


# In[32]:


#setting the size for the plot
f,ax=plt.subplots(figsize=(10,5))

cmap = sns.cubehelix_palette(12, start=1, rot=-.70,as_cmap=True, dark=0.55, light=0.95, reverse=False)
sns.kdeplot(fb_data['Total Interactions'],fb_data['Lifetime Post Total Reach'], 
            cmap=cmap, shade=True);

plt.xlim(-100,400)
plt.ylim(-5000,15000)


# ## Diverging Color Palettes
# Befor we discuss this, let us first see a diverging color palette

# In[288]:


#A Color Brew Palette
sns.palplot(sns.color_palette("BrBG", 9))


# In[289]:


#A matplotlib palette
sns.palplot(sns.color_palette("coolwarm", 9))


# We have seen two plots above. What do we observe from this?
# * These are very similar to the sequential color palette we see above 
# * The low intensity color is in the centre with high intensities on either sides, unlike the sequential palette. These colors are of similar intensity and brightness.
# * There are two shades of color ranges on either sides from the centre.
# * While calling the palette too, the names have 2 shades defined.
# * Notice that 'n' is odd, as there is a well defined midpoint
# 
# 
# These plots are best suited for data spread over a wide range, where both the high and low values are of interest. There will be a well-defined mid point. For example, plotting the efficiency of a device between -40 to +80 degrees Celsius.
# 

# #### Custom diverging palettes
# * Use the Seaborn diverging_palette() and create your own custom palette.
# * Run choose_diverging_palette() from an ipython notebook for assistance
# * The function uses "husl" system to create well balanced color maps
# 

# Lets view the options in diverging palettes. This time, instead of just seeing it, we shall store the object in 'h' and use this in our next plot.

# In[46]:


h=sns.choose_colorbrewer_palette('diverging')


# In[47]:


g = sns.PairGrid(fb_data,
                 vars=["comment", "like", "share"],
                 hue="Type",
                 palette=h)
g.map_offdiag(plt.scatter) 
g.map_diag(sns.kdeplot) 
g.add_legend()


# We defined 'h' as the palette 'coolwarm'. In that case, if we plot the same graph as above with the palette name itself, we would expect the plots to be the same. Let's verify that.

# In[37]:


g = sns.PairGrid(fb_data,
                 vars=["comment", "like","share"],
                 hue="Type",
                 palette="coolwarm")
g.map_offdiag(plt.scatter) 
g.map_diag(sns.kdeplot) 
g.add_legend()


# No. Our assumption was wrong. We see that although the palettes are same, the colour choices depend on the 'n' value. We set it as 12 in 'h' and thus the plot was plotted with the first 4 of the 12 colours. But when you passed the entire palette into the plot function, it automatically created 4 colours from the palette and used them. This can be verified by viewing te same pallete with n as 4.

# In[292]:


#Specifying two colours, the saturation and lightness value, and the number of shades needed.
sns.palplot(sns.diverging_palette(150, 350, s=90, l=40, n=11)


# In[293]:


# Reverse the palette to make the centre dark,
sns.palplot(sns.diverging_palette(150, 350, s=90, l=40, n=11, center="dark"))


# ### And there we go!! One small question from what we have learnt so far! Can we make a sequential palette by using the diverging palette function??
# 
# * Both hues should be of same color
# * n should be even (not a necessary condition though)
# 

# In[39]:


sns.palplot(sns.diverging_palette(350, 350, s=90, l=40, n=12))


# The result is like a sequential palette placed next to its mirror image.

# In[ ]:




