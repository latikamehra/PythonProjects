'''
Created on Aug 7, 2019

@author: latikamehra
'''

import matplotlib.pyplot as plt
import os
import numpy as np

class LineGraph:
    def __init__(self, fileNamePrefix, title, x_label,y_label):
        
        self.defaultYAxisValue = 0 # Value to be plotted if an x-axis value is missing from the data dictionary # This is to display a common x-axis line for multiple line plots
        self.pl = plt
        self.x_fontSize = 10
        self.rotation = 30
        self.fileNamePrefix= os.path.dirname(os.path.abspath(__file__))+"/../charts/"+fileNamePrefix
        
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        

    def plotMultipleLineGraphs(self, linesPerGraph, dictOfDict): # The data is constructed as a Dictionary of Dictionary such that Dict[line] = {x-axis_data => y-axis_data}
        
        allPossibleXaxisValues = self.fetchAllPossibleXaxisValues(dictOfDict)
        
        numOfGraphs = int(len(dictOfDict.keys())/linesPerGraph)+1
              
        i=1
        for ln in sorted(dictOfDict.keys()) :
            lastSaveFlag = False
            j = int(i/linesPerGraph)
            fileName = self.fileNamePrefix+"_"+str(j)+".png"
            
            lbl = ln
            lineDict = dictOfDict[ln]
            
            self.plotSingleLine(lbl, lineDict, allPossibleXaxisValues)
            
            if i%linesPerGraph == 0 : # Check if the end of the graph has been reached 
                self.saveGraph(fileName)
                lastSaveFlag = True
                
            i += 1
        
        
        if lastSaveFlag == False :
            fileName = self.fileNamePrefix+"_"+str(j+1)+".png"    
            self.saveGraph(fileName)  # Save the last graph that may contain less than 'linesPerGraph' line  
        
        plt.show()  
        

    def plotSingleLine(self, label, lineDict, allPossibleXaxisValues):
        x_axis_lst=allPossibleXaxisValues
        y_axis_lst=[]

        for xaxis in allPossibleXaxisValues:
            if xaxis in lineDict.keys():
                y_axis_lst.append(lineDict[xaxis])  
            else:
                y_axis_lst.append(self.defaultYAxisValue)
        
        np_x = np.array(x_axis_lst)
        np_y = np.array(y_axis_lst)
        
        
        plt.xticks(rotation=self.rotation)
        plt.plot(np_x, np_y, label=label)
        
        #print(label)
        #print(np_x)
        #print(np_y)
        
        
    def saveGraph(self, fileName):
        
        plt.title(self.title)
        plt.xlabel(self.x_label, fontsize=self.x_fontSize)
        plt.ylabel(self.y_label, fontsize=self.x_fontSize)
        plt.legend()
        plt.savefig(fileName, bbox_inches='tight')
        
        plt.figure() # Change figure after saving the graph
        
    
    def fetchAllPossibleXaxisValues(self,dictOfDict):
        xAxisLst = []
        for axesDict in dictOfDict.values(): #dictOfDict's values have x-axis+y-axis dictionary
            for xAxis in axesDict.keys(): # the keys of the axes dictionary have x-axis values
                xAxisLst.append(xAxis)
            
        dedupedList = set(xAxisLst) # Create a set of all x-axis values without duplicates
        xAxisLst = sorted(list (dedupedList)) # Convert that de-duped set back to a sorted list
            
        return xAxisLst  
