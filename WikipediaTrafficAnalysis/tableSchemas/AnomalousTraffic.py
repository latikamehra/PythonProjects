'''
Created on Jul 20, 2019

@author: latikamehra
'''

from . import SchemaName

dbSchema = SchemaName.schema
tableName = dbSchema+".Anomalous_Traffic"

schema = [("id", "integer"),
          ("date", "varchar(10)"), 
          ("view_count", "integer")]