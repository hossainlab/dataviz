# Grids

Grids are general types of plots that allow you to map plot types to rows and columns of a grid, this helps you create similar plots separated by features.

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

iris = sns.load_dataset('iris')

iris.head()


## PairGrid

Pairgrid is a subplot grid for plotting pairwise relationships in a dataset.

# Just the Grid
sns.PairGrid(iris)

# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)

# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

## Pairplot

pairplot is a simpler version of PairGrid (you'll use quite often)

sns.pairplot(iris)

sns.pairplot(iris,hue='species',palette='rainbow')

## Facet Grid

FacetGrid is the general way to create grids of plots based off of a feature

tips = sns.load_dataset('tips')

tips.head()

# Just the Grid
g = sns.FacetGrid(tips, col="time", row="smoker")

g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")

g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Notice hwo the arguments come after plt.scatter call
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

## JointGrid

JointGrid is the general version for jointplot() type grids, for a quick example:

g = sns.JointGrid(x="total_bill", y="tip", data=tips)

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)