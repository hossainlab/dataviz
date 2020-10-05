# Introduction to Cufflinks

This library binds the power of plotly with the flexibility of pandas for easy plotting.

## Import Libraries 

import pandas as pd 
import numpy as np 
import cufflinks as cf 
import chart_studio.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 

## Config 

cf.set_config_file(theme='ggplot',sharing='public',offline=True)

## Enable Notebook Mode

 init_notebook_mode(connected=True)

## Let's a Create a Simple Plot 

cf.datagen.lines().iplot(kind='scatter',xTitle='Dates',yTitle='Returns',title='Cufflinks - Line Chart')