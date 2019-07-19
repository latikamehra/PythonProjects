'''
Created on Jul 16, 2019

@author: latikamehra
'''

    
from dbOps import Postgres


tbl = "RadAge"

schema = [("id", "integer"),
          ("name", "varchar(50)"), 
          ("age", "integer")]

dt = [("1","Jonny","47"), 
      ("2","Thom","49"), 
      ("3","Colin","49"), 
      ("4","Ed O'Brien","50"), 
      ("5","Phil","51") ]



    
    
    
 
pg = Postgres.postgres(tbl,schema)

pg.connect()

pg.createTable()

pg.writeData(dt)

pg.cleanEntireTable()

pg.dropTable()