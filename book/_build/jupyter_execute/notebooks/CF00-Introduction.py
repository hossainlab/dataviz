# Introduction to Cufflinks

This library binds the power of plotly with the flexibility of pandas for easy plotting.

import pandas as pd 
import numpy as np 
import cufflinks as cf 
import chart_studio.plotly as py


%reload_ext autoreload
%autoreload 2

init_notebook_mode(connected=True)

cf.set_config_file(theme='ggplot',sharing='public',offline=False)

df = pd.read_csv('../data/iris.csv')

df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].iplot(kind='box')

cf.datagen.lines(1,1000).iplot()

df=cf.datagen.lines(4,1000)
df.iplot()