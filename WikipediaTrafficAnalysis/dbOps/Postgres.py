'''
Created on Jul 16, 2019

@author: latikamehra
'''

import psycopg2


class postgres():
    
    def __init__(self, tableName, schemaTupleList):
        self.hostname = 'localhost'
        self.username = 'latikamehra'
        self.password = ''
        self.database = 'latikamehra' 
        
        self.tableName = tableName
        self.schemaTupleList = schemaTupleList
        
        self.colsTpl = None
        self.insertableColTpl = None
        self.setColTpl() # Construct the tuple of columns & tuple of non-auto-generated columns
        
        self.colListStr = None
        self.insertableColLstStr = None # List of Columns that are NOT auto-generated
        self.schemaListString = None
        self.execmanyStr = None
        self.setSchemaStrings()  # Construct the string constructed as ordered column names & column types
        
        self.conn = None
        self.cur = None
    
    def connect(self):
        try :
            self.conn = psycopg2.connect(host=self.hostname, user=self.username, password=self.password, database=self.database)
            self.cur = self.conn.cursor()
        except Exception as e :
            print ("Failed to connect to the Postgres database")
            print (e)
            
    
    def closeConns(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
            
    def createTable(self):
        sqlBase = "CREATE TABLE IF NOT EXISTS {0} ({1})"
        
        sql = sqlBase.format(self.tableName, self.schemaListString)
        
        try:
            print ("Executing the following create statement :\n\t"+sql)
            self.cur.execute(sql)
            self.conn.commit()
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to create the table "+self.tableName)
            print (e)
            
            
            
    def cleanEntireTable(self):
        sqlBase = "DELETE FROM {0}"
        
        sql = sqlBase.format(self.tableName)
        
        try:
            print ("Executing the following DELETE statement :\n\t"+sql)
            self.cur.execute(sql)
            self.conn.commit()
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to delete the table "+self.tableName)
            print (e)
        
        
    def deleteSpecificRows(self, whereClause):
        sqlBase = "DELETE FROM {0} {1}"
        
        sql = sqlBase.format(self.tableName, whereClause)
        
        try:
            print ("Executing the following DELETE statement :\n\t"+sql)
            self.cur.execute(sql)
            self.conn.commit()
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to delete the table "+self.tableName)
            print (e)
            
        
    def dropTable(self):
        sqlBase = "DROP TABLE IF EXISTS {0}"
        
        sql = sqlBase.format(self.tableName)
        
        try:
            print ("Executing the following DROP statement :\n\t"+sql)
            self.cur.execute(sql)
            self.conn.commit()
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to drop the table "+self.tableName)
            print (e)
            
            
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
            print ("Executing the following READ statement :\n\t"+sql)
            self.cur.execute(sql)  
            res = self.cur.fetchall()   
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to read data from the database")
            print (e)
            
        resDictLst = self.constrResDicLst(colsTpl, res)    
        
        return resDictLst
    
    

            
    def insertData(self, dataTplLst):
        sqlBase = "INSERT INTO {0} ({1}) VALUES ({2})"
        
        sql = sqlBase.format(self.tableName, self.insertableColLstStr, self.execmanyStr)
        
        dataDictLst = self.constructDataDictList(dataTplLst)
        
        try :
            print ("Executing the following INSERT statement :\n\t"+sql)
            self.cur.executemany(sql, dataDictLst)  
            self.conn.commit()    
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to write data to the database")
            print (e)
            
            
    def updateData(self, setStmnt, whereStmnt):
        sqlBase = "UPDATE {0} {1} {2}"
        
        sql = sqlBase.format(self.tableName, setStmnt, whereStmnt)
        
        try :
            print ("Executing the following INSERT statement :\n\t"+sql)
            self.cur.execute(sql)  
            self.conn.commit()    
            print ("Statement successfully executed\n\n")
        except Exception as e:
            print ("Failed to update data to the database")
            print (e)
                       
            
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
                dictBit[self.insertableColTpl[i]] = d[i] 
            
            dtDictLst.append(dictBit)
            
        #print (dtDictLst)
            
        return dtDictLst  
    
    
    def constrResDicLst(self, colsTpl, res):
        resDictLst = []
        
        for row in res :
            dictBit = {}
            for i in range(len(row)):
                dictBit[colsTpl[i].strip()] = row[i]
            
            resDictLst.append(dictBit)
            
        return resDictLst
        
 
            
