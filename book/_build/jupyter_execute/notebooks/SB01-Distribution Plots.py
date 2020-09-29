# Distribution Plots
Let's discuss some plots that allow us to visualize the distribution of a data set.


___
## Imports

import seaborn as sns
%matplotlib inline

## Data
Seaborn comes with built-in data sets!

tips = sns.load_dataset('tips')

tips.head()

## Distplot

The distplot shows the distribution of a univariate set of observations.

sns.distplot(tips['total_bill'])

# To remove the kde layer and just have the histogram 
sns.distplot(tips['total_bill'],kde=False,bins=30)

## Jointplot

`jointplot()` allows you to basically match up two distplots for bivariate data. With your choice of what **kind** parameter to compare with: 
* “scatter” 
* “reg” 
* “resid” 
* “kde” 
* “hex”

### Scatter 

sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')

### Hex 

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

### Regression 

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

## Pairplot

pairplot will plot pairwise relationships across an entire dataframe (for the numerical columns) and supports a color hue argument (for categorical columns). 

sns.pairplot(tips)

# separate by sex and color 
sns.pairplot(tips,hue='sex',palette='coolwarm')

## Rugplot

`rugplots` are actually a very simple concept, they just draw a dash mark for every point on a univariate distribution. They are the building block of a KDE plot

sns.rugplot(tips['total_bill'])

## kdeplot

kdeplots are [Kernel Density Estimation plots](http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth). These KDE plots replace every single observation with a Gaussian (Normal) distribution centered around that value. For example:

# Don't worry about understanding this code!
# It's just for the diagram below
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)

# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")

So with our tips dataset:

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])