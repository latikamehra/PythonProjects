'''
Created on Aug 13, 2019

@author: latikamehra
'''

import matplotlib.pyplot as plt 
from yellowbrick.features import ParallelCoordinates, Rank2D
import pandas as pd
import numpy as np
from commonOps import StackedBar, NormalizedParallelCoordinates, PearsonCorrelation

plt.rcParams['figure.figsize'] = (20, 10)

classes = ['Survived', 'Not-Survived']

dt = [[1, 42, 1000, 'M'], [0, 80, 2000, 'T'], [1, 5, 0, 'F'], [0, 20, 10,'F'] , [0, 20, 10,'M']]

ds = pd.DataFrame(dt, columns=['Status', 'Age', 'Salary', 'Sex'])

#ds.Status = ds.Status.replace(to_replace=[1,0], value=classes )
ds = ds.replace({'Status' : {1: 'Survived', 0: 'Not-Survived'}})

ds_norm = ds.copy()

num_features = ['Age', 'Salary']

PearsonCorrelation.create(ds, num_features, "PearsonCorrelation")

NormalizedParallelCoordinates.create(ds, num_features, classes, "ParallelCoordinates")

fig, axs = plt.subplots(nrows=1, ncols=1)

StackedBar.create(axs, ds, 'Sex', 'Status')
plt.show()

#print (ds_norm)

