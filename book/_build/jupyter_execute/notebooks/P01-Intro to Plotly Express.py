# Intro to Plotly Express
In this notebook I'll try to explore gapminder dataset using interactive data visualization library called Plotly. About the Dataset:
[Data Source](https://www.gapminder.org/tools/#$state$time$value=2007;;&chart-type=bubbles)


## Import Libraries 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px # for visualization 
import plotly.offline as py 
import plotly.graph_objs as go 
from plotly.figure_factory import create_table # for creating nice table 

## Loading the Dataset 

# load built-in gapminder dataset from plotly 
gapminder = px.data.gapminder() 

# examine first few rows 
gapminder.head() 

## Creating a Table 

# create a publication quality table 
table = create_table(gapminder.head(10))
py.iplot(table)

## Quick Visualizations with Bar Charts

# filtering data for Canada and store into a variable called canada_data 
canada_data = px.data.gapminder().query("country == 'Canada' ")

# create bar charts 
fig = px.bar(canada_data, x='year', y='pop', height=400)
fig.show() 

# let's add color by lifeExp and other parameters 
fig = px.bar(canada_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'}, height=400)
fig.show() 

## Plot Life Expectency vs GDP Per Capita

# filter 2007 data only from dataset 
gapminder2007 = gapminder.query('year == 2007')

# create scatter plot 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp')
fig.show() 

# color by continent 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent')
fig.show() 

##  Create Interactive Bubble Charts

# create a bubble chart 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60)
fig.show() 

# hover name 
fig = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                 hover_name='country')
fig.show() 

##  Create Interactive Animations and Facet Plots

# create a facet plot 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                hover_name='country', facet_col='continent')
fig.show() 

# log scale on x-axis 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=60, 
                hover_name='country', facet_col='continent', log_x=True)
fig.show()

# let's add animation 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, 
                hover_name='country', log_x=True, animation_frame='year',
                 animation_group='country', range_x=[25, 10000], range_y=[25,90])
fig.show()

# customize the labels 
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, 
                hover_name='country',log_x=True, animation_frame='year',
                 animation_group='country', range_x=[25, 10000], range_y=[25,90], 
                labels=dict(pop="Population", gdpPercap="GDP Per Capita", lifeExp="Life Expectency"))
fig.show()

##  Represent Geographic Data as Animated Maps

# create a map using line_geo()
fig = px.line_geo(gapminder.query('year == 2007'), locations='iso_alpha', color='continent', projection='orthographic')
fig.show() 

# create a map using choropleth
fig = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', 
                    animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig.show() 

## 10: Using Plotly Template in Any Graphs

# print available themes or template 
import plotly.io as pio
pio.templates

# let's use plotly_dark in our previous bar chart 
fig = px.bar(canada_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='plotly_dark')
fig.show()

# seaborn
fig = px.bar(canada_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='seaborn')
fig.show()

# ggplot2 
fig = px.bar(canada_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of Canada'},
             height=400, template='ggplot2')
fig.show()