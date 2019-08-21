'''
Created on Aug 7, 2019

@author: latikamehra
'''

import csv

class ReadCSV:
    def __init__(self, csvFile):
        self.csvFile = csvFile
    
    def fetchHeaders(self):
        fl = open(self.csvFile)
        csvStream = csv.reader(fl)
        i=0
        for row in csvStream:
            i += 1
            headerList = row
            if i>0 :
                break
        
        fl.close()
        return headerList
    
    def getData(self, startRow=2, numRows=-1):
        fl = open(self.csvFile)
        csvStream = csv.reader(fl)
        i=1
        dataSet = []
        for row in csvStream:
            
            if i>=startRow and (numRows==-1 or i<(startRow+numRows)):
                dataSet.append(row)
                
            i += 1
            
        fl.close()
        return dataSet



if __name__ == "__main__":
    rc = ReadCSV("/Users/latikamehra/Documents/AppleMusicPlayActivity.csv")
    rc.fetchHeaders()
    ds = rc.getData(numRows=5)
    for row in ds:
        print (row)
    
    