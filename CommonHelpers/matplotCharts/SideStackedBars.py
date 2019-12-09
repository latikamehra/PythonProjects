'''
Created on Aug 13, 2019

@author: latikamehra
'''

import numpy as np
from operator import add
import matplotlib.pyplot as plt

def createFrequencyGraph(df, legendDim, xAxisDim, axs = plt.subplots(1,1)[1]):
    
    listOfLegends = df[legendDim].unique()
    listOfXaxis = df[xAxisDim].unique().tolist()
    
    
    leg = [[],[]]
    grpByYandXaxesByLegendDim = df.groupby(legendDim)
    p = [None]*len(listOfLegends)
    
    cumVals = [0]*len(listOfXaxis)
    
    for i, y in enumerate(listOfLegends):
        newVals = []
        grpByYandXaxes = (grpByYandXaxesByLegendDim.get_group(y)).groupby(xAxisDim)
        
        for x in listOfXaxis:
            try:
                dt = grpByYandXaxes.get_group(x)
                sz = dt.agg(np.size)[0]
            except KeyError:
                sz = 0
            
            newVals.append(sz)   
        
        p[i] = axs.bar(listOfXaxis,newVals,bottom=cumVals)
        cumVals = list(map(add,cumVals,newVals))
            
        leg[0].append(p[i][0])
        leg[1].append(y)
    
    axs.set_title(legendDim)
    axs.set_ylabel("Counts")
    axs.legend((leg[0]), leg[1])
    
    plt.show()
    
    
def createCountGraph(df, legendDim, xAxisDim, yAxisDim, axs = plt.subplots(1,1)[1]):
    width = 0.2
    listOfXaxis = df[xAxisDim].unique().tolist()
    
    legends = [[],[]]
    grpByXaxes = df.groupby(xAxisDim)
    
    for i, x in enumerate(listOfXaxis):
        grpByXaxesAndLegend = (grpByXaxes.get_group(x)).groupby(legendDim)
        
        widthCounter = 0
        for leg, grp in grpByXaxesAndLegend:
            try:
                
                #dt = grp.get_group(leg)
                sz = grp[yAxisDim].sum()
                
                widthCounter += width
                plts = axs.bar(i+widthCounter,sz)
                
                legends[0].append(plts[0])
                legends[1].append(leg)
                
            except KeyError:
                sz = 0 

    axs.set_xlabel(listOfXaxis)
    axs.set_title(legendDim)
    axs.set_ylabel("Counts")
    axs.legend((legends[0]), legends[1])
    
    plt.show()