#!/usr/bin/env python
# coding: utf-8

# #### The Path class
# Path represents a series of possibly disconnected, possibly closed, line and curve segments

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()


# #### Defining a segment
# * The Path class takes in an array of vertices followed by an equal-length array of 'codes' or vertex types
# * The first code is always MOVETO which moves to the corresponding vertex (think of moving the cursor to that point)
# * There is a LINETO function which will draw a line from the 'cursor' to the corresponding vertex and then moves the 'cursor' to that vertex

# In[2]:


fig, ax = plt.subplots()

p = patches.PathPatch(Path([(0.1, 0.1), (0.8, 0.8), (0.8, 0.1), (0.4, 0.2)],
                             [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]),
                       fill=None)

ax.add_patch(p)

plt.show()


# #### The CLOSEPOLY code
# This closes the polygon by drawing a line from the current position to the starting point in the list of vertices. Here, the closing line is drawn from (0.8, 0.1) to (0.1, 0.1) to close the polygon - thus 

# In[3]:


fig, ax = plt.subplots()

p = patches.PathPatch(Path([(0.1, 0.1), (0.8, 0.8), (0.8, 0.1), (0.4, 0.2)],
                             [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]),
                       fill=None)

ax.add_patch(p)

plt.show()


# ### Bezier curves
# One can plot a quadratic or cubic Bezier curve using Path

# #### Quadratic Bezier curve
# This requires three points to work with - a start point, control point and end point - and is referenced by CURVE3
# * In our example, those 3 points are (0.8, 0.8), (0.8, 0.1), (0.4, 0.2)
# * We call CURVE3 twice here to complete the quadratic curve. Alternatively, we can call it once followed by MOVETO

# In[4]:


fig, ax = plt.subplots()

p = patches.PathPatch(Path([(0.1, 0.1), (0.8, 0.8), (0.8, 0.1), (0.4, 0.2)],
                             [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3]),
                       fill=None)

ax.add_patch(p)

plt.show()


# #### Using MOVETO instead of a second CURVE3
# The same curve is drawn here as the same points are used for the Bezier curve

# In[5]:


fig, ax = plt.subplots()

p = patches.PathPatch(Path([(0.1, 0.1), (0.8, 0.8), (0.8, 0.1), (0.4, 0.2)],
                             [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.MOVETO]),
                       fill=None)

ax.add_patch(p)

plt.show()


# #### Cubic Bezier curve
# This requires for points to work with - a start point, 2 control points and an end point - and is referenced by CURVE4
# * In our example, those 4 points are (0.8, 0.8), (0.8, 0.1), (0.4, 0.2), (0.1, 0.1)
# * We call CURVE4 just once followed by 2 calls to MOVETO

# In[6]:


fig, ax = plt.subplots()

p = patches.PathPatch(Path([(0.1, 0.1), (0.8, 0.8), (0.8, 0.1), (0.4, 0.2), (0.1, 0.1)],
                             [Path.MOVETO, Path.LINETO, Path.CURVE4, Path.MOVETO, Path.MOVETO]),
                       fill=None)

ax.add_patch(p)

plt.show()


# In[ ]:




