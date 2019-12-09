'''
Created on Aug 7, 2019

@author: latikamehra

'''

import matplotlib.pyplot as plt
import numpy as np
import os

class BarSubplots:
    def __init__(self, numOfBarsPerPlot, fileNamePrefix, title,x_label,y_label):
        plt.rcParams['figure.figsize'] = (32, 18)
        self.legendSize = 6
        self.label_fontSize = 15
        self.title_fontSize = 17
        self.xtick_rotation = 30
        self.xtick_fontsz = 7
        self.ytick_fontsz = 10
        self.subplotHeightSpace = 0.2
        self.subplotWidthSpace = 0.7
 

        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.fileName= os.path.dirname(os.path.abspath(__file__))+"/../charts/"+fileNamePrefix+".png"
        
        self.numOfBarsPerPlot = numOfBarsPerPlot
        self.numOfSubplots = 0
        self.ncols = 3
        self.nrows = 0
        
    def plotSingleSubplot(self,  x_axis_lst, y_axis_lst , axs = plt.subplots(1,1)[1]): 
        indx = np.arange(len(x_axis_lst))
        
        axs.barh(indx, y_axis_lst)
        axs.set_yticks(indx)
        axs.set_yticklabels(x_axis_lst)
        axs.invert_yaxis()
        
        #for x in axs.get_xticklabels():
        #    x.set_rotation(self.xtick_rotation) # Rotate each of the x-axis ticks
            

    def plotGraph(self, x_axis_lst,  y_axis_lst):
        self.numOfSubplots = len(x_axis_lst)//self.numOfBarsPerPlot + 1
        self.nrows = self.numOfSubplots//self.ncols + min(self.numOfSubplots%self.ncols, 1)
        
        
        self.fig, axes = plt.subplots(nrows=self.nrows, ncols=self.ncols)
        
        
        for i in range(self.numOfSubplots-1):
            
            row = i//self.ncols
            col = i%self.ncols
            
            x_list = x_axis_lst[self.numOfBarsPerPlot*i : self.numOfBarsPerPlot*(i+1)]
            y_list = y_axis_lst[self.numOfBarsPerPlot*i : self.numOfBarsPerPlot*(i+1)]
            
            self.plotSingleSubplot( x_list,y_list, axes[row,col]  )
         
        # Plot the last subplot which may have number of x-axis elements less than 'numOfBarsPerPlot'
        j = self.numOfSubplots-1
        row = j//self.ncols
        col = j%self.ncols

        x_list = x_axis_lst[self.numOfBarsPerPlot*(j) :]
        y_list = y_axis_lst[self.numOfBarsPerPlot*(j) :]
        self.plotSingleSubplot( x_list, y_list , axes[row,col] )
        
        self.showAndSave()
        
    def showAndSave(self):
          
        self.fig.suptitle(self.title, fontsize=self.title_fontSize)
        self.fig.text(0.5,0.05, self.y_label, ha="center", va="center", fontsize=self.label_fontSize)
        self.fig.text(0.05,0.5, self.x_label, ha="center", va="center", rotation=90, fontsize=self.label_fontSize)
        
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=self.subplotWidthSpace, hspace=self.subplotHeightSpace)
        
        plt.savefig(self.fileName)
        plt.show()

