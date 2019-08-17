'''
Created on Aug 14, 2019

@author: latikamehra
'''

from yellowbrick.features import ParallelCoordinates
from . import NormalizeNumericalDataSet as nnds

def create(df, num_features, classes, fileName):
    df_norm = nnds.generate(df, num_features)

    x = df_norm[num_features].as_matrix()
    y = df_norm.Status.as_matrix()
       
    vis = ParallelCoordinates(classes=classes, features=num_features)
    vis.fit(x,y)
    vis.poof(outpath="../charts/"+fileName+".png")