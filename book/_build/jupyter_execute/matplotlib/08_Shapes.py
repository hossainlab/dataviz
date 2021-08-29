#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Make use of the patch module to draw a shape
# * Patches allows rendering of 2D objects including geometric shapes, arrows
# * When creating a rectangle, the first argument is a tuple with the bottom-left coordinates
# * The next two coordinates are the width and height of the rectangle
# * The fill parameter represents whether the shape will be filled with a color. We choose to leave the square empty
# * Note that though we're plotting a square it appears as a rectangle due to the differing aspect ratios of the X and Y axes

# In[2]:


fig, ax = plt.subplots()

ax.add_patch(
    patches.Rectangle(
        (0.1, 0.1),
        0.5,
        0.5,
        fill=False 
    )
)

plt.show()


# #### Use the aspect parameter for the axis to fix the aspect ratio
# Now the X and Y axes are on the same scale
# * Other options are 'auto' or a number
# * A number n means the height will be n times the width

# In[3]:


fig, ax = plt.subplots()

ax.set_aspect(aspect='equal')

ax.add_patch(
    patches.Rectangle(
        (0.1, 0.1),
        0.5,
        0.5,
        fill=False
    )
)

plt.show()


# #### Color the shape
# * facecolor defines the color to fill the shape with
# * edgecolor sets the color of the edge
# 
# There are a number of colors which can be set using the name. For a full list of these colors, check out this link: <br />
# https://matplotlib.org/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py

# In[4]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

ax.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   
        0.5,         
        0.5,          
        facecolor='yellow',
        edgecolor='green'
    )
)

plt.show()


# #### Drawing multiple sqares
# * We use an iterator to define and add rectangles to our subplot
# * We set different patterns inside those squares with the hatch parameter
# * Note that the default facecolor is blue

# In[5]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.3, 0.6,
        hatch='.'
    ),
    patches.Rectangle(
        (0.5, 0.1), 0.3, 0.6,
        hatch='\\',
        fill=False
    ),
]:
    ax.add_patch(p)
    
plt.show()


# #### Setting the alpha value for shapes
# * Each rectangle has a different transparency level
# * Note that alpha=None is the same as alpha=1.0
# * The third rectangle is not visible, as the default xlim (and ylim) is 1

# In[6]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6,
        alpha=None,
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6,
        alpha=1.0
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6,
        alpha=0.6
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6,
        alpha=0.1
    ),
]:
    ax.add_patch(p)

plt.show()


# #### Setting the xlim so that all rectangles are visible

# In[7]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6,
        alpha=None,
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6,
        alpha=1.0
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6,
        alpha=0.6
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6,
        alpha=0.1
    ),
]:
    ax.add_patch(p)

ax.set_xlim(0,1.5)

plt.show()


# #### Specifying the colors in different formats
# * facecolor=None sets it to the default (blue) color
# * facecolor="none" means the facecolor is empty

# In[8]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6,
        facecolor=None
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6,
        facecolor='none'
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6,
        facecolor='red'
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6,
        facecolor='#00ffff'
    ),
]:
    ax.add_patch(p)
    
ax.set_xlim(0,1.5)
plt.show()


# #### Shapes with edgecolor
# * Setting the edgecolor without a facecolor sets the facecolor value to 'none'
# * Note that the default edgecolor is black

# In[9]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6, fill=False,
        edgecolor=None
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6, fill=False,
        edgecolor='none'
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6, fill=False,
        edgecolor='red'
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6, fill=False,
        edgecolor='#00ffff'
    ),
]:
    ax.add_patch(p)
        
ax.set_xlim(0,1.5)
plt.show()


# #### Changing the line width 
# The default linewidth is 1.0

# In[10]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6, fill=False,
        linewidth=None
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6, fill=False,
        linewidth=0
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6, fill=False,
        linewidth=0.5
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6, fill=False,
        linewidth=3
    ),
]:
    ax.add_patch(p)
    
ax.set_xlim(0,1.5)
plt.show()


# #### Different types of linestyles
# This defines the type of line representing the edge

# In[11]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Rectangle(
        (0.1, 0.1), 0.2, 0.6, fill=False,
        linestyle='solid'   # Default
    ),
    patches.Rectangle(
        (0.4, 0.1), 0.2, 0.6, fill=False,
        linestyle='dashed'
    ),
    patches.Rectangle(
        (0.7, 0.1), 0.2, 0.6, fill=False,
        linestyle='dashdot'
    ),
    patches.Rectangle(
        (1.0, 0.1), 0.2, 0.6, fill=False,
        linestyle='dotted'
    ),
]:
    ax.add_patch(p)
    
ax.set_xlim(0,1.5)
plt.show()


# #### Circles
# * The parameters when drawing a circle are the center coordinates and the radius
# * The hatch and facecolor work the same way as they do for rectangles

# In[12]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Circle(
        (0.1, 0.4), 0.1,
        hatch='/'
    ),
    patches.Circle(
        (0.5, 0.4), 0.1,
        hatch='*',
        facecolor='red'
    ),
    patches.Circle(
        (0.9, 0.4), 0.1,
        hatch='\\',
        facecolor='green'
    ),
    patches.Circle(
        (0.5, 0.7), 0.1,
        hatch='//',
        fill=False 
    ),
]:
    ax.add_patch(p)
    
plt.show()


# #### The color parameter and setting the hatch color
# * The color parameter is used to set the facecolor, edgecolor and hatch color - hence the hatch pattern cannot be seen for the green circle
# * Note that the edgecolor and hatch color are the same - there is no separate hatchcolor attribute

# In[13]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

for p in [
    patches.Circle(
        (0.1, 0.4), 0.1,
        hatch='/'
    ),
    patches.Circle(
        (0.5, 0.4), 0.1,
        hatch='*',
        facecolor='red'
    ),
    patches.Circle(
        (0.9, 0.4), 0.1,
        hatch='\\',
        color='green'
    ),
    patches.Circle(
        (0.5, 0.7), 0.1,
        hatch='//',
        fill=False,
        edgecolor = 'blue'
    ),
]:
    ax.add_patch(p)
    
plt.show()


# #### Polygons
# The patches module can also draw other 2-D shapes such as a polygon
# * The parameters include a 2-D array with the x,y coordinates of the polygon vertices
# * The points are listed in sequential order. i.e. point 1 will connect to point 2 which is connected to point 3 etc. 
# * By default, the polygon is 'closed' - the last point is connected to the first point
# 

# In[14]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

polygon = patches.Polygon([[0.1, 0.1],
                           [0.2, 0.8], 
                           [0.5, 0.7], 
                           [0.8, 0.1], 
                           [0.4, 0.3]],
                          fill=False)
                   
ax.add_patch(polygon)
    
plt.show()
                   


# #### "Open" polygon
# In this case the first and last points are not automatically connected

# In[15]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

polygon = patches.Polygon([[0.1, 0.1],
                           [0.2, 0.8], 
                           [0.5, 0.7], 
                           [0.8, 0.1], 
                           [0.4, 0.3]],
                          closed=False,
                          fill=False)
                   
ax.add_patch(polygon)
    
plt.show()           


# #### Arrows
# * The patches module can also generate other 2-D shapes such as arrows
# * Note these are not arrow lines - but 2-D arrow shapes

# 4 parameters are required:
# * The first two are the x,y coordinates of the center of the arrow tail
# * The next two are the x,y coordinates of the base (not the tip) of the arrow head 

# In[16]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

polygon = patches.Arrow(0.1, 0.2, 
                        0.7, 0.7)

ax.add_patch(polygon)
    
plt.show()


# #### Arrow width
# * The default arrow width is 1.0 which equates to 0.2 on the axis at the tail and 0.6 at the head
# * Here we halve the width to 0.5 which is 0.1 at the tail and 0.3 at the head

# In[17]:


fig, ax = plt.subplots()
ax.set_aspect(aspect='equal')

polygon = patches.Arrow(0.1, 0.2, 
                        0.7, 0.7,
                        width=0.5)

ax.add_patch(polygon)
    
plt.show()


# In[ ]:




