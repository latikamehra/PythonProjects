'''
Created on Aug 7, 2019

@author: latikamehra

'''

import matplotlib.pyplot as plt
import numpy as np
import os

class BarGraph:
    def __init__(self,fileNamePrefix,title,x_label,y_label):
        self.x_fontSize = 10
        self.rotation = 30
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.fileName= os.path.dirname(os.path.abspath(__file__))+"/../charts/"+fileNamePrefix+".png"
        


    def plotGraph(self, x_axis_lst,  y_axis_lst):
        plt.title(self.title)
        plt.xlabel(self.x_label, fontsize=self.x_fontSize)
        plt.ylabel(self.y_label, fontsize=self.x_fontSize)
        
        index = np.arange(len(x_axis_lst))

        plt.bar(index, y_axis_lst)
        
        plt.xticks(index, x_axis_lst, fontsize=self.x_fontSize, rotation=self.rotation)
        
        plt.savefig(self.fileName, bbox_inches='tight')
        plt.show()

