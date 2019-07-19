'''
Created on Jul 16, 2019

@author: latikamehra
'''

    
from dbOps import Postgres


tbl = "RadAge"

'''
schema = [("id", "integer"),
          ("name", "varchar(50)"), 
          ("age", "integer")]

dt = [("1","Jonny","47"), 
      ("2","Thom","49"), 
      ("3","Colin","49"), 
      ("4","Ed O'Brien","50"), 
      ("5","Phil","51") ]

'''


schema = [("id", "serial"),
          ("name", "varchar(50)"), 
          ("age", "integer")]

dt = [("Jonny","47"), 
      ("Thom","49"), 
      ("Colin","49"), 
      ("Ed O'Brien","50"), 
      ("Phil","51") ]

    
    
    
 
pg = Postgres.postgres(tbl,schema)

pg.connect()

pg.createTable()

pg.cleanEntireTable()

pg.insertData(dt)

#pg.deleteSpecificRows("WHERE name in ('"+dt[2][1]+"')")
pg.updateData("SET age=46", "WHERE id=1")

resDictLst = pg.readData("*", "WHERE name='Jonny'")

print (resDictLst)

#pg.cleanEntireTable()

#pg.dropTable()