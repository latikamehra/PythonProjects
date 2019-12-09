'''
Created on Aug 28, 2019

@author: latikamehra
'''

import pandas as pd
from commonOps import StackedBar
import matplotlib.pyplot as plt

dt = [[1, 42, 1000, 'M'], [0, 80, 2000, 'T'], [1, 5, 0, 'F'], [0, 20, 10,'F'] , [0, 20, 10,'M']]

ds = pd.DataFrame(dt, columns=['Status', 'Age', 'Salary', 'Sex'])


ds = ds.replace({'Status' : {1: 'Survived', 0: 'Not-Survived'}})

grps = ds.groupby('Status')

#print (grps.size())
#print (grps.size().reset_index())

cnts = grps.size().reset_index(name='Counts')

x = cnts['Status']
 
y = cnts['Counts']

newDF = pd.DataFrame(cnts, columns=['Status', 'Counts'])

fig, axs = plt.subplots(1,2, figsize=(15,15))

StackedBar.create(axs[0], ds, 'Sex', 'Status')

plt.show()

print (x)
print (y)

#for name, grp in grps:
    #print (name)
    #print (grp) 
