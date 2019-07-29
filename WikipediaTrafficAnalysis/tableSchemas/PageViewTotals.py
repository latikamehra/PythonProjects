'''
Created on Jul 20, 2019

@author: latikamehra
'''

from . import SchemaName

dbSchema = SchemaName.schema
tableName = dbSchema+".Page_View_Totals"

schema = [("id", "serial"),
          ("page_name", "varchar(100)"), 
          ("total_views", "integer"),
          ("daily_avg_views", "integer"),
           ("last_updated_on", "varchar(100)")]