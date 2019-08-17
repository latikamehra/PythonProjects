'''
Created on Aug 14, 2019

@author: latikamehra
'''

from yellowbrick.features import Rank2D
from . import NormalizeNumericalDataSet as nnds

def create(df, features, fileName):
    df_norm = nnds.generate(df, features)
    x = df_norm[features].as_matrix()
    ran = Rank2D(features=features, algorithm='pearson')
    ran.fit(x)
    ran.transform(x)
    ran.poof(outpath="../charts/"+fileName+".png")
