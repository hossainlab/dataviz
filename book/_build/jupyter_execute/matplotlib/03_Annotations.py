#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# In[2]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

plt.show()


# #### Basic annotation
# * The first param is the annotation text
# * xy represents the coordinate the annotation should be pointing to
# * xytext is the position where the annotation text begins (defaults to xy if not specified)
# * arrowprops allows the specification of a FancyArrowPatch object for the arrow to draw for the annotation. All the keyword arguments for that can be found here: https://matplotlib.org/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch

# In[3]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('min value', 
            xy=(1, 2), 
            xytext=(1.5,2.0),
            arrowprops=dict(color='g'))

plt.show()


# #### Changing the text position changes the arrow orientation

# In[4]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('min value', 
            xy=(1,2), 
            xytext=(1,3),
            arrowprops=dict(color='g'))

plt.show()


# #### Setting the arrow specifications
# Just like any shape, we can define several specifications for the arrow. Here we set the facecolor, edgecolor and alpha value. 

# In[5]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('min value', 
            xy=(1,2), 
            xytext=(1,3),
            arrowprops=dict(facecolor='y', edgecolor='green', alpha=0.3))

plt.show()


# #### Set the color for the annotation text

# In[6]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('min value', 
            xy=(1,2), 
            xytext=(1,3),
            arrowprops=dict(facecolor='y', edgecolor='green', alpha=0.3),
            color='red',style='italic')

plt.show()


# #### Arrow annotation with a point
# We draw a point with a red circle and add our arrow annotation to it. Note that the arrowhead overlaps with the dot

# In[7]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('significant point', 
            xy=(2, 4), 
            xytext=(2.0, 2.5),
            arrowprops=dict(color='g'))

ax.plot([2], [4], "ro")

plt.show()


# #### The shrink parameter
# The FancyArrowPatch allows the arrow to be reduced in size by specifying a shrink factor. Here we shrink the arrow at the ends by 10%. This ensures the arrowhead does not overlap with the point

# In[8]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3],
        [2, 4, 6])

ax.annotate('significant point', 
            xy=(2, 4), 
            xytext=(2.0, 2.5),
            arrowprops=dict(color='g', shrink=0.1))

ax.plot([2], [4], "go")

plt.show()


# ### Advanced Annotation
# Annotating with Text with Box

# In[9]:


import numpy as np


# #### Define two sets of plots which we shall use

# In[10]:


np.random.seed(0)

x1 = -1 + np.random.randn(100)
y1 = -1 + np.random.randn(100)

x2 = 1 + np.random.randn(100)
y2 = 1 + np.random.randn(100)


# #### Draw those plots in a figure
# This is just to illustrate what the plot looks like. We will go on to add box annotations to such a figure

# In[11]:


fig, ax = plt.subplots()

ax.scatter(x1, y1, color='r')
ax.scatter(x2, y2, color='g')

plt.show()


# #### Define a binding box for the box annotation
# Define the properties of the binding box for our annotation. This binding box is a FancyBboxPatch object:
# https://matplotlib.org/api/_as_gen/matplotlib.patches.FancyBboxPatch.html
# * boxstyle of 'square' represents a rectangle
# * the box will be white in color with a transparency of 0.5

# #### Add the text annotation within a binding box
# * The first two params of ax.text() represent the center coordinates of the text provided ha and va are center
# * The font size of our text is set to 20
# * Use the binding box definition which we just created to wrap around the text

# In[12]:


fig, ax = plt.subplots()

ax.scatter(x1, y1, color='r')
ax.scatter(x2, y2, color='g')

bbox_props = dict(boxstyle='square', 
                  facecolor='w', 
                  alpha=0.5)

ax.text(-2, -2, 
        'Sample A', 
        ha='center', 
        va='center', 
        size=20,
        bbox=bbox_props)

ax.text(2, 2, 
        'Sample B', 
        ha='center', 
        va='center', 
        size=20,
        bbox=bbox_props)


# ### Text within an arrow
# The binding box can also be an arrow with its own properties

# #### Define the properties of our Arrow binding box
# * An 'rarrow' is a right-pointing arrrow
# * The facecolor is cyan, edgecolor is blue, and the edge is thicker than the default 1
# * We set an alpha value for this box

# #### Add the new annotation in an Arrow to our axis
# * The annotation text is 'Direction' and it's centered at (0,0)
# * The 'rotation' specifies the angle of the arrow to the X axis
# * The font size is 15
# * We use the properties we just defined for the arrow binding box

# In[13]:


fig, ax = plt.subplots()

ax.scatter(x1, y1, color='r')
ax.scatter(x2, y2, color='g')

ax.text(-2, -2, 
        'Sample A', 
        ha='center', 
        va='center', 
        size=20,
        bbox=bbox_props)

ax.text(2, 2, 
        'Sample B', 
        ha='center', 
        va='center', 
        size=20,
        bbox=bbox_props)

arrow_bbox_props = dict(boxstyle='rarrow', 
                        facecolor='#EBF5FB', 
                        edgecolor='b', 
                        linewidth=2,
                        alpha=0.7)
ax.text(0, 0, 
        'Direction', 
        ha='center', 
        va='center', 
        rotation=60,
        size=15,
        bbox=arrow_bbox_props)


# ### Different forms of binding boxes
# The available forms are larrow, rarrow, darrow (bidrectional arrow), circle, round (rounded rectangle), round4 (a curvier rounded rectangle), sawtooth (rectangle with sawtooth edges) etc. All the shapes can be found here:
# https://matplotlib.org/gallery/shapes_and_collections/fancybox_demo.html
# 
# We use a few of these shapes here

# In[14]:


sawtooth_bbox_props = dict(boxstyle='sawtooth', 
                           facecolor='#ABEBC6', 
                           alpha=0.8)


# In[15]:


round4_bbox_props = dict(boxstyle='round4', 
                         facecolor='#EBDEF0', 
                         alpha=0.8)


# In[16]:


arrow_bbox_props = dict(boxstyle='darrow', 
                        facecolor='#FDEDEC', 
                        alpha=0.5)


# In[17]:


fig, ax = plt.subplots()

ax.scatter(x1, y1, color='r')
ax.scatter(x2, y2, color='g')

ax.text(-2, -2, 
        'Sample A', 
        ha='center', 
        va='center', 
        size=20,
        bbox=sawtooth_bbox_props)

ax.text(2, 2, 
        'Sample B', 
        ha='center', 
        va='center', 
        size=20,
        bbox=round4_bbox_props)

ax.text(0, 0, 
        'Direction', 
        ha='center', 
        va='center', 
        rotation=60,
        size=15,
        bbox=arrow_bbox_props)


# In[ ]:




