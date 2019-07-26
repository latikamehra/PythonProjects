'''
Created on Jul 23, 2019

@author: latikamehra
'''

import tableSchemas.AnomalousTraffic
import tableSchemas.PageViewTotals

a = tableSchemas.AnomalousTraffic
p = tableSchemas.PageViewTotals

a_date = a.schema[1][0]
p_page_name = p.schema[1][0]
a_view_count = a.schema[2][0]
p_avg_vc = p.schema[3][0]
p_total_views = p.schema[2][0]
a_table = a.tableName
p_table = p.tableName
a_id = a.schema[0][0]
p_id = p.schema[0][0]

'''
SQL to be constructed as an equivalent of :
select 
a.date,
array_agg(p.page_name) as page_names,
array_agg(a.view_count/p.avg_vc) as spike_factor
from wikidata.anomalous_traffic a 
join wikidata.page_view_totals p 
on a.id=p.id
group by a.date
having count(a.id)>1
order by a.date
'''

sql = """select 
a."""+a_date+""",
array_agg(p."""+p_page_name+""") as page_names,
array_agg(a."""+a_view_count+"""/p."""+p_avg_vc+""") as spike_factor
from """+a_table+""" a 
join """+p_table+""" p 
on a."""+a_id+"""=p."""+p_id+"""
group by a."""+a_date+"""
having count(a."""+a_id+""")>1
order by a."""+a_date+""""""

