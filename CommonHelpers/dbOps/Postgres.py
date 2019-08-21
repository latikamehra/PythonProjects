'''
Created on Jul 16, 2019

@author: latikamehra
'''

import psycopg2
import config.Postgres
import logging
from formatters import AppLogger


class postgres():
    
    def __init__(self, tableName=None, schemaTupleList=None, verbose=False):
        self.log = AppLogger.logger.getChild(__name__)
        pg = config.Postgres
        self.hostname = pg.hostname
        self.username = pg.username
        self.password = pg.password
        self.database = pg.database
        
        self.tableName = tableName
        self.schemaTupleList = schemaTupleList
        
        self.colsTpl = None
        self.insertableColTpl = None
        if schemaTupleList is not None :
            self.setColTpl() # Construct the tuple of columns & tuple of non-auto-generated columns
        
        self.colListStr = None
        self.insertableColLstStr = None # List of Columns that are NOT auto-generated
        self.schemaListString = None
        self.execmanyStr = None
        if schemaTupleList is not None :
            self.setSchemaStrings()  # Construct the string constructed as ordered column names & column types
        
        self.conn = None
        self.cur = None
        
        self.verbose = verbose
    
    def connect(self):
        try :
            self.conn = psycopg2.connect(host=self.hostname, user=self.username, password=self.password, database=self.database)
            self.cur = self.conn.cursor()
        except Exception as e :
            self.log.error ("Failed to connect to the Postgres database")
            self.log.error (e)
            
    
    def closeConns(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        
    def psql(self, tp, sql):
        if self.verbose == True :
            stmnt = "{0}Successfully executed the following "+tp+" statement :{1}"+sql+"{2}"
            stmnt = stmnt.format("\n"+"-"*100+"\n", "\n\t","\n"+"-"*100+"\n")
            self.log.error (stmnt)
            
    def createTable(self):
        optionalSchema = self.tableName.split(".")
        if len(optionalSchema) > 1 :
            schemaName = optionalSchema[0]
            self.cur.execute("CREATE SCHEMA IF NOT EXISTS "+schemaName)
        
        sqlBase = "CREATE TABLE IF NOT EXISTS {0} ({1})"
        
        sql = sqlBase.format(self.tableName, self.schemaListString)
        
        try:
            self.log.debug(sql)
            self.cur.execute(sql)
            self.conn.commit()
            self.psql("CREATE", sql)
        except Exception as e:
            self.log.error ("Failed to create the table "+self.tableName)
            self.log.error (e)
            
            
            
    def cleanEntireTable(self):
        sqlBase = "DELETE FROM {0}"
        
        sql = sqlBase.format(self.tableName)
        
        try:
            self.log.debug(sql)
            self.cur.execute(sql)
            self.conn.commit()
            self.psql("DELETE", sql)
        except Exception as e:
            self.log.error ("Failed to delete the table "+self.tableName)
            self.log.error (e)
        
        
    def deleteSpecificRows(self, whereClause):
        sqlBase = "DELETE FROM {0} {1}"
        
        sql = sqlBase.format(self.tableName, whereClause)
        
        try:
            self.log.debug(sql)
            self.cur.execute(sql)
            self.conn.commit()
            self.psql("DELETE", sql)
        except Exception as e:
            self.log.error ("Failed to delete the table "+self.tableName)
            self.log.error (e)
            
        
    def dropTable(self):
        sqlBase = "DROP TABLE IF EXISTS {0}"
        
        sql = sqlBase.format(self.tableName)
        
        try:
            self.log.debug(sql)
            self.cur.execute(sql)
            self.conn.commit()
            self.psql("DROP", sql)
        except Exception as e:
            self.log.error ("Failed to drop the table "+self.tableName)
            self.log.error (e)
            
    def executeReadStatement(self, sql):
        
        try :
            self.log.debug(sql)
            self.cur.execute(sql)  
            res = self.cur.fetchall()   
            self.psql("READ", sql)
        except Exception as e:
            self.log.error ("Failed to read data from the database")
            self.log.error (e)
            
        return res
        
           
    def readData(self, cols, *whereClause):
        sqlBase = "SELECT {0} FROM {1} "
        
        if type(cols) is tuple : # If the list of columns is presented as a tuple then stick to it 
            colsTpl = cols
        else:  # Assume the columns have been provided as a string of comma separated string 
            if cols.strip() == "*" : # If an asterisk is given all the columns in the table have to be fetched data for
                colsTpl = self.colsTpl
            else :
                colsTpl = cols.split(",")
            
        colListStr = ",".join(colsTpl)
        
        sql = sqlBase.format(colListStr,self.tableName)
        
        for w in whereClause:
            sql += " "+w+" "  
        
        try :
            self.log.debug(sql)
            self.cur.execute(sql)  
            res = self.cur.fetchall()   
            self.psql("READ", sql)
        except Exception as e:
            self.log.error ("Failed to read data from the database")
            self.log.error (e)
            
        resDictLst = self.constrResDicLst(colsTpl, res)    
        
        return resDictLst
    
    

            
    def insertData(self, dataTplLst):
        sqlBase = "INSERT INTO {0} ({1}) VALUES ({2})"
        
        sql = sqlBase.format(self.tableName, self.insertableColLstStr, self.execmanyStr)
        
        dataDictLst = self.constructDataDictList(dataTplLst)
        
        try :
            self.log.debug(sql)
            self.log.debug(dataDictLst)
            self.cur.executemany(sql, dataDictLst)  
            self.conn.commit()    
            self.psql("INSERT", sql)
        except Exception as e:
            self.log.error ("Failed to write the following "+str(len(dataDictLst))+" rows to the database: ")
            self.log.error (dataDictLst)
            self.log.error (e)
            
            
    def updateData(self, setStmnt, whereStmnt):
        sqlBase = "UPDATE {0} {1} {2}"
        
        sql = sqlBase.format(self.tableName, setStmnt, whereStmnt)
        
        try :
            self.log.debug(sql)
            self.cur.execute(sql)  
            self.conn.commit()    
            self.psql("UPDATE", sql)
        except Exception as e:
            self.log.error ("Failed to update data to the database")
            self.log.error (e)
                       
            
    def setColTpl(self):
        colLst = []
        insColLst = []

        for sch in self.schemaTupleList :
            colLst.append(sch[0])
            if sch[1].strip().lower() != "serial":
                insColLst.append(sch[0])
            
        self.colsTpl = tuple(colLst)
        self.insertableColTpl = tuple(insColLst)
        
            
            
    def setSchemaStrings(self):
        schemaStrLst = []  # Start a list that will contain strings of column names & column types that will eventually be joined with a comma
        colStrLst = []   # Start a list that will contain strings of only column names that will eventually be joined with a comma
        execmanyStrLst = [] # Start a list that will contain strings of column names preceded by %( and followed by )s
        insertableColStrLst = [] # Start a list that will contain strings of only those columns which are NOT auto-generated that will eventually be joined with a comma
        
        for col_tpl in self.schemaTupleList:  # Read the schema list that contains tuples constructed as (column_name , columns_type)
            
            schemaStrBit = " ".join(col_tpl)  # Join column name and column type with a space
            schemaStrLst.append(schemaStrBit)  # Add the string containing present column name and type to a list
            
            colStrLst.append(col_tpl[0])  # Add the string containing only the present column name to a list
            
            if col_tpl[1].strip().lower() != "serial" : # If the column type is NOT serial then that column has to be added to the list of columns that will be required for Insert operation
                insertableColStrLst.append(col_tpl[0])
                execmnBit = "%("+col_tpl[0]+")s" # Add the required string bits to the column name to prepare for the executeMany statement
                execmanyStrLst.append(execmnBit)
            
            
            
        self.schemaListString = " , ".join(schemaStrLst)
        self.colListStr = " , ".join(colStrLst)
        self.insertableColLstStr = " , ".join(insertableColStrLst)
        self.execmanyStr = " , ".join(execmanyStrLst)
        
        
        
    def constructDataDictList(self, dataTplLst): # Construct a list of dictionary DS for the data sent as a list of tuples
        dtDictLst = []
        
        for d in dataTplLst:
            dictBit = {}
            
            for i in range(len(self.insertableColTpl)):
                #self.log.debug (i)
                #self.log.debug(self.insertableColTpl[i])
                #self.log.debug (d[i])
                dictBit[self.insertableColTpl[i]] = d[i] 
            
            dtDictLst.append(dictBit)
            
        #self.log.debug (dtDictLst)
            
        return dtDictLst  
    
    
    def constrResDicLst(self, colsTpl, res):
        resDictLst = []
        
        for row in res :
            dictBit = {}
            for i in range(len(row)):
                dictBit[colsTpl[i].strip()] = row[i]
            
            resDictLst.append(dictBit)
            
        return resDictLst
        
 
            
