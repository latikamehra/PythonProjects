'''
Created on Aug 7, 2019

@author: latikamehra
'''

from dbOps import Postgres
from csvOps import ReadCSV
from formatters import AppLogger
import logging

class Load:
    
    def __init__(self, csvFile, tableName, lvl=logging.INFO):
        AppLogger.initiate("LoadCSVtoPostgres", lvl)
        self.logger = AppLogger.logger
        self.csvFile = csvFile
        self.tableName = tableName
        
        self.readCSV = ReadCSV.ReadCSV(self.csvFile)
        self.pg = None
        self.schemaTplList = None
        
        
    def constructTableSchema(self, headerList):
        self.schemaTplList = [tuple(("id", "serial"))]
        for header in headerList:
            header = header.replace(" ","_")
            self.schemaTplList.append(tuple((header, "varchar(500)")))
        
    def createTable(self, resetFlag=False):  
        headerList = self.readCSV.fetchHeaders()
        self.constructTableSchema(headerList)
        
        self.pg = Postgres.postgres(tableName=self.tableName, schemaTupleList=self.schemaTplList)
        self.pg.connect()
        if resetFlag==True : self.pg.dropTable()
        self.pg.createTable()
        
        
    def insertData(self):
        dataSetLstLst = [1] #Instantiate data list to be inserted with a dummy value for the while loop's 1st iteration
        stRow = 2
        blockSize = 500
        attemptedRows = 0
        while len(dataSetLstLst)>0: 
            dataSetLstLst = self.readCSV.getData(startRow=stRow,  numRows=blockSize) # Read the CSV in incremental chunks the size of blockSize
            self.pg.insertData(dataSetLstLst)
            stRow += blockSize
            
            attemptedRows += len(dataSetLstLst)
         
        insertedRows = self.pg.executeReadStatement("select count(*) from "+self.tableName)[0][0]   
        
        if  insertedRows!=attemptedRows:
            self.logger.error("Attempted to insert "+str(attemptedRows)+" rows into the "+self.tableName+" table, but only "+str(insertedRows)+" rows could be successfully inserted")
            self.logger.error("Check the log file "+self.logger.handlers[0].baseFilename+" for the DB errors that have occurred")
        else:
            self.logger.info("Successfully inserted all "+str(attemptedRows)+" rows into the "+self.tableName)    
        
        

        
if __name__ == "__main__":
    lvl = lvl=logging.INFO
    lc = Load("/Users/latikamehra/Documents/AppleMusicPlayActivity.csv", "data_analysis.apple_music_activity", lvl)
    lc.createTable(True)
    lc.insertData()
    lc.pg.closeConns()
    
    