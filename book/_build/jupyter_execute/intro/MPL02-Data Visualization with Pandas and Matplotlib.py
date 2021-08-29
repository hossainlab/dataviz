#!/usr/bin/env python
# coding: utf-8

# # Data Visualization with Pandas and Matplotlib

# In[1]:


# import library 
import pandas as pd 
import matplotlib.pyplot as plt 

# display plot in the notebook 
get_ipython().run_line_magic('matplotlib', 'inline')

# set figuresize and fontsize 
plt.rcParams['figure.figsize'] = (8,6) 
plt.rcParams['font.size'] = 14 


# In[2]:


# read data 
drink_cols = ["country", 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv("../data/drinks.csv", header=0, names=drink_cols, na_filter=False)


# ## Data Exploration

# In[3]:


# examine first few rows 
drinks.head() 


# In[4]:


# observations and columns 
drinks.shape


# In[5]:


# data structure 
drinks.info() 


# In[6]:


# numerical summary 
drinks.describe() 


# ##  Histogram: show the distribution of a numerical variable

# In[7]:


# sort the beer columns and split it into 3 groups 
drinks.beer.sort_values().values


# In[8]:


# compare with histogram 
drinks.beer.plot(kind="hist", bins=3);


# In[9]:


# try more bins 
drinks.beer.plot(kind="hist", bins=20); 


# In[10]:


# add title and labels 
drinks.beer.plot(kind="hist", bins=20, title="Histogram of Beer Servings")
plt.xlabel("Beer Survings") 
plt.ylabel("Frequency")
# show plot 
plt.show() 


# In[11]:


# compare with density plot(smooth version of a histogram) 
drinks.beer.plot(kind="density", xlim=(0, 500));


# ## Scatter Plot: show the relationship between two numerical variables

# In[12]:


# select the beer and wine columns and sort by beer 
drinks[["beer", "wine"]].sort_values(by="beer").values


# In[13]:


# comapre with scatter plot 
drinks.plot(kind="scatter", x="beer", y="wine"); 


# In[14]:


# add transparency 
drinks.plot(kind='scatter', x="beer", y="wine", alpha=0.3); 


# In[15]:


# vary point color by spirit servings 
drinks.plot(kind="scatter", x="beer", y="wine", c="spirit", colormap="Blues"); 


# In[16]:


# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']]); 


# In[17]:


# increase figure size 
# scatter matrix of 3 numerical columns 
pd.plotting.scatter_matrix(drinks[['beer', 'wine', 'spirit']], figsize=(10,8)); 


# ##  Bar Plot: show a numerical comparison across different categories

# In[18]:


# count the number of countries in each continent 
drinks.continent.value_counts()


# In[19]:


# compare with bar plot 
drinks.continent.value_counts().plot(kind="bar"); 


# In[20]:


# calculate the mean alcohol amounts for each continent 
drinks.groupby('continent').mean() 


# In[21]:


# side-by-side bar plots 
drinks.groupby('continent').mean().plot(kind='bar'); 


# In[22]:


# drop the liters column
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar'); 


# In[23]:


# stacked bar plots 
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True); 


# ## Box Plot: show quartiles (and outliers) for one or more numerical variables
# __Five-Number Summary__
# * min = minimum value
# * 5% = first quartile (Q1) = median of the lower half of the data
# * 50% = second quartile (Q2) = median of the data
# * 75% = third quartile (Q3) = median of the upper half of the data
# * max = maximum value
# (More useful than mean and standard deviation for describing skewed distributions)
# * Interquartile Range (IQR) = Q3 - Q1
# 
# __Outliers__ 
# * below Q1 - 1.5 * IQR
# * above Q3 + 1.5 * IQR

# In[24]:


# sort the spirit column 
drinks.spirit.sort_values().values 


# In[25]:


# show five-number summary of spirit 
drinks.spirit.describe() 


# In[26]:


# compare with boxplot 
drinks.spirit.plot(kind='box');  


# In[27]:


# include multiple variables 
drinks.drop('liters', axis=1).plot(kind='box'); 


# ## Line Plot: show the trend of a numerical variable over time

# In[28]:


# read ufo data 
ufo = pd.read_csv("../data/ufo.csv")
ufo['Time'] = pd.to_datetime(ufo.Time) 
ufo['Year'] = ufo.Time.dt.year 


# In[29]:


# examine first few rows  
ufo.head() 


# In[30]:


# observations and columns 
ufo.shape 


# In[31]:


# data structure 
ufo.info() 


# In[32]:


# numerical summary 
ufo.describe()  


# In[33]:


# count the number of ufo reports each year (and sort by year)
ufo.Year.value_counts().sort_index() 


# In[34]:


# compare with line plot 
ufo.Year.value_counts().sort_index().plot();


# In[35]:


# don't use a line plot when there is no logical ordering 
drinks.continent.value_counts().plot(kind='line'); 


# ## Grouped Box Plots: show one box plot for each group

# In[36]:


# remainder: boxplot of beer survings 
drinks.beer.plot(kind='box'); 


# In[37]:


# boxplot of beer survings group by continent 
drinks.boxplot(column='beer', by='continent'); 


# In[38]:


# boxplot of all numerical columns group by continent 
drinks.boxplot(by='continent'); 


# ## Grouped Histograms: show one histogram for each group

# In[39]:


# remainder: histogram of beer survings 
drinks.beer.plot(kind='hist', bins=20); 


# In[40]:


# histogram of beer  survings group by continent 
drinks.hist(column='beer', by='continent'); 


# In[41]:


# share the x-axis 
drinks.hist(column='beer', by='continent', sharex=True); 


# In[42]:


# share the x and y axis 
drinks.hist(column='beer', by='continent', sharex=True, sharey=True); 


# In[43]:


# change the layout 
drinks.hist(column='beer', by='continent', sharex=True, layout=(2, 3));


#  ## Assorted Functionality

# In[44]:


# saving a plot to a file 
drinks.beer.plot(kind='hist', bins=20, title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Freequency")
plt.savefig("beer_survings.png") # .png, .tiff, .pdf, .jpeg 


# In[45]:


# list available plot style 
plt.style.available


# In[46]:


# use plot style: ggplot 
plt.style.use('ggplot')


# In[47]:


# histogram of beer survings in ggplot style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")


# In[48]:


# use plot style: ggplot 
plt.style.use('seaborn') 


# In[49]:


# histogram of beer survings in seaborn style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")


# In[50]:


# use plot style: ggplot 
plt.style.use('fivethirtyeight') 


# In[51]:


# histogram of beer survings in fivethirtyeight style 
drinks.beer.plot(kind="hist", title="Histogram of Beer Survings")
plt.xlabel("Beer Survings")
plt.ylabel("Frequnecy")

