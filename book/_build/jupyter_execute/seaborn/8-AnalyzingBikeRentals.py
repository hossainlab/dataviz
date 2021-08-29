#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# We will now import a dataset from the UCI Machine Learning repository. The data is deals with bike rentals where people can pick up bikes from one location and drop them off at any other designated location, as convenient to them. 

# In[4]:


bike_data=pd.read_csv('datasets/day.csv',
                     sep=r'\s*,\s*', engine='python')


# In[5]:


bike_data.head()


# The data has the following fields
# - instant: record index
# - dteday : date
# - season : season (1:springer, 2:summer, 3:fall, 4:winter)
# - yr : year (0: 2011, 1:2012)
# - mnth : month ( 1 to 12)
# - hr : hour (0 to 23)
# - holiday : weather day is holiday or not (extracted from [Web Link])
# - weekday : day of the week
# - workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
# + weathersit : 
# - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
# - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
# - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
# - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
# - temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
# - atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
# - hum: Normalized humidity. The values are divided to 100 (max)
# - windspeed: Normalized wind speed. The values are divided to 67 (max)
# - casual: count of casual users
# - registered: count of registered users
# - cnt: count of total rental bikes including both casual and registered

# In[6]:


bike_data.describe()


# We want to study this data and predict the trends of shared bikes, and maybe provide a guide to tourists about when bikes would be easily available for rent. This is clearly a machine learning problem where we will first use a training dataset, figure out relationships and then apply the same algorithms on new data.
# 
# Before we move on to our machine learning model, let us first quickly explore the dataset to see if any relationship exists using Seaborn. 

# ## First, let's get an idea of the demand for bike sharing. 
# From the data description we just saw above, the average number of bikes rented was around 4500 each day.
# Plotting a histogram with the number of bikes rented,

# In[8]:


f, ax=plt.subplots(figsize=(15,5))

sns.distplot(bike_data['cnt'],bins=75, kde=False, rug=True);


# We see that the demand for bikes is mostly between the range of 4000-5000, with a peak of about 4600 from the graph. This matches with the average we observed. There are some days with demand as less as about a 100, while the max demand on any given day is about 8400.

# ## Let us try to see how the number of bikes rented varies with every day of the year. 
# Our dataset has about 2 years worth of data. Lets plot a jointplot of the instant versus the bike count. The instant is a measure of

# In[47]:


sns.jointplot(x='instant', y='cnt', data=bike_data, size=8)


# We see that the demand for bikes starts with a small number, increases at about instant 200 that corresponds to mid year,and drops down towards the end of the year. The same pattern follow in the second year too, with a max at instant 600 range corresponding to mid second year. There is an extra peak in the second half of the second year.
# We can see that there is maximum demand for rental bikes during mid year and least during the start and end of the year. Let us confirm this by plotting the demand for the different months.
# 

# In[48]:


sns.jointplot(x='mnth', y='cnt', data=bike_data, size=8)


# Our analysis is perfectly correct. The maximum demand is in the months of 6-8, which is mid year, i.e. June-July. The peak seen in the second half of the second year falls in the 9th month, as is clear from the above plot. 

# ## Let us now try to see how the demand varies across the week.

# In[9]:


sns.pairplot(bike_data, 
             size=5, aspect=0.9, 
             x_vars=["holiday","weekday","workingday"],
             y_vars=["cnt"],
             kind="reg",
             hue="season")


# The above are three graphs of the bike count plotted versus whether the day is a holiday, weekday or working day respectively.
# 
# * From the second plot, the number of bikes hired seem to be almost the same on all days of the week. 
# * From the third plot, days weekdays seem to have more requests than weekends/holidays(workingday=1).
# * The first plot clearly shows that the demand for bikes on rent is most during days that are not holidays. 
# * Comparing the above two points, it looks like the demand on weekends is also similar, but slightly lesser than other weekdays.
# 
# From the above analysis, the dataset seems to point to the bikes rented by the working class to travel to and from the workplace, or subway stations. This explains why there is more demand during weekdays than on holidays.

# ** What is very interesting to note here is that while we would have expected the number of bikes rented to be dependent on the day of the week, the regression line fits show that the demand is more dependent on the season of the year than on the day of the week. **
# 
# * The highest demand is in season 3, fall
# * Next comes season 2, summer
# * Followed by season 4, winter
# * And the least demand is in season 1, spring
# 

# *To confirm our above observation, lets plot the count versus the season of the year*

# In[61]:


sns.jointplot(x='season', y='cnt', data=bike_data, size=8)


# We see that this perfectly matches our analysis from the previous graph.
# 
# ## Does the weather condition also play a role in the number of bike rentals?

# In[65]:


sns.pairplot(bike_data, 
             size=5, aspect=0.9, 
             x_vars=["temp","atemp","hum","windspeed"],
             y_vars=["cnt"],
             hue="season")


# The first two plots are the number of bike rentals versus the temperature and the 'feels-like' temperature. These seem similar and we can say that there is not much change in rental pattern. More the temperature of the day, higher are the number of people choosing to hire a bike, there is a significant number of bike rentals even when temperatures are low.
# 
# When the days are very dry, there are hardly any bike rentals. When the humidity crosses a limit of 0.4, bikes are in demand.
# 
# The windspeed also influences bike rentals to an extent. Windspeeds of 0.1 to 0.3 have a high demand for bike rentals. As the speed becomes higher, it probably gets too cold to ride and the number of rentals reduces.
# 
# 

# In[ ]:




