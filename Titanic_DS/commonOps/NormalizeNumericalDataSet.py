'''
Created on Aug 14, 2019

@author: latikamehra
'''

def generate(df, num_features):
    for feat in num_features:
        df[feat] = (df[feat] - df[feat].min())/(df[feat].max() - df[feat].min())
        
    return (df)