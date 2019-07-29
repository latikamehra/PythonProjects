'''
Created on Jul 23, 2019

@author: latikamehra
'''

import tableSchemas.PageViewTotals


p = tableSchemas.PageViewTotals

p_page_name = p.schema[1][0]
p_avg_vc = p.schema[3][0]
p_total_views = p.schema[2][0]
p_table = p.tableName
p_id = p.schema[0][0]

'''
SQL to be constructed as an equivalent of :
select A.page_name, TRUNC(A.daily_avg_views::decimal/B.min_vc,2) as vc_ratio
from 
(select page_name, daily_avg_views
from wikidata.page_view_totals) A ,
(select MIN(daily_avg_views) as min_vc 
from wikidata.page_view_totals) B
order by daily_avg_views
'''

sqlBase = """select A.{0}, TRUNC(A.{1}::decimal/B.min_vc,2) as vc_ratio
from 
(select {0}, {1}
from {2}) A ,
(select MIN({1}) as min_vc 
from {2}) B
order by {1}"""

sql = sqlBase.format(p_page_name,p_avg_vc,p_table)

