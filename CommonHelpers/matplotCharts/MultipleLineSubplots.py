'''
Created on Aug 7, 2019

@author: latikamehra
'''

import matplotlib.pyplot as plt
import os
import numpy as np

class LineSubPlots:
    def __init__(self, fileNamePrefix, title, x_label,y_label):
        plt.rcParams['figure.figsize'] = (32, 18)
        self.defaultYAxisValue = 0 # Value to be plotted if an x-axis value is missing from the data dictionary # This is to display a common x-axis line for multiple line plots
        
        self.legendSize = 6
        self.label_fontSize = 15
        self.title_fontSize = 17
        self.xtick_rotation = 30
        self.xtick_fontsz = 7
        self.ytick_fontsz = 10
        self.subplotHeightSpace = 0.1
        self.subplotWidthSpace = 0.1
        
        
        plt.axis('tight')
        plt.rc('xtick', labelsize=self.xtick_fontsz)
        plt.rc('ytick', labelsize=self.ytick_fontsz)

        self.fileNamePrefix= os.path.dirname(os.path.abspath(__file__))+"/../charts/"+fileNamePrefix
        
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        
        self.numOfPlotsPerRow = 5
        self.subplotRow = 0
        self.subplotCol = 0
        self.numOfPlots = 0
        self.rowsReqd = 0 
        self.fig = None
        self.axs = None
        

    def plotMultipleLineGraphs(self, linesPerGraph, dictOfDict): # The data is constructed as a Dictionary of Dictionary such that Dict[line] = {x-axis_data => y-axis_data}
        
        allPossibleXaxisValues = self.fetchAllPossibleXaxisValues(dictOfDict)
        
        self.numOfPlots = int(len(dictOfDict.keys())/linesPerGraph)+1
        
        self.rowsReqd = int(self.numOfPlots/self.numOfPlotsPerRow) + min(self.numOfPlots%self.numOfPlotsPerRow, 1)
        
        self.fig, self.axs = plt.subplots(self.rowsReqd, self.numOfPlotsPerRow, sharex=True)
        
              
        i=1
        for ln in sorted(dictOfDict.keys()) :
            plotLabeledFlag = False
            j = int(i/linesPerGraph)
            fileName = self.fileNamePrefix+".png"
            
            lbl = ln
            lineDict = dictOfDict[ln]
            
            self.plotSingleLine(lbl, lineDict, allPossibleXaxisValues)
            
            #print (self.subplotRow, self.subplotCol)
            if i%linesPerGraph == 0 : # Check if the end of the graph has been reached 
                plotLabeledFlag = True
                self.labelSubplot()
                if self.subplotCol == (self.numOfPlotsPerRow - 1):
                    self.subplotCol = 0
                    self.subplotRow += 1
                else:
                    self.subplotCol += 1
                
            i += 1
            
            
        if plotLabeledFlag == False :
            self.labelSubplot() # Label the last plot that may contain less than 'linesPerGraph' line  
        
        self.saveGraph(fileName)
        

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
        
        self.axs[self.subplotRow, self.subplotCol].plot(np_x, np_y, label=label)
        
        
        
        #print(label)
        #print(np_x)
        #print(np_y)
    
    def labelSubplot(self):
        for x in self.axs[self.subplotRow, self.subplotCol].get_xticklabels():
            x.set_rotation(self.xtick_rotation) # Rotate each of the x-axis ticks
            
        self.axs[self.subplotRow, self.subplotCol].legend(prop={'size': self.legendSize})
        
    def saveGraph(self, fileName):
        
        self.cleanUnusedSubplots() # Clean-up sub-plots which will not be used
        
        self.fig.suptitle(self.title, fontsize=self.title_fontSize)
        self.fig.text(0.5,0.05, self.x_label, ha="center", va="center", fontsize=self.label_fontSize)
        self.fig.text(0.05,0.5, self.y_label, ha="center", va="center", rotation=90, fontsize=self.label_fontSize)
        
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=self.subplotWidthSpace, hspace=self.subplotHeightSpace)
        
        plt.savefig(fileName)
        
        plt.show()  
        
    
    def fetchAllPossibleXaxisValues(self,dictOfDict):
        xAxisLst = []
        for axesDict in dictOfDict.values(): #dictOfDict's values have x-axis+y-axis dictionary
            for xAxis in axesDict.keys(): # the keys of the axes dictionary have x-axis values
                xAxisLst.append(xAxis)
            
        dedupedList = set(xAxisLst) # Create a set of all x-axis values without duplicates
        xAxisLst = sorted(list (dedupedList)) # Convert that de-duped set back to a sorted list
            
        return xAxisLst  
    
    def cleanUnusedSubplots(self):
        unusedCnt = (self.numOfPlotsPerRow * self.rowsReqd) % self.numOfPlots
        lastRow = self.rowsReqd - 1
        lastCol = self.numOfPlotsPerRow - 1
        
        for i in range(unusedCnt) :
            self.axs[lastRow, lastCol].plot()
            self.labelSubplot()
            #self.fig.delaxes(self.axs[lastRow, lastCol])
            lastCol -= 1
        
