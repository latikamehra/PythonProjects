'''
Created on Aug 7, 2019

@author: latikamehra
'''

sql = """select 
lpad(extract(year from event_received_timestamp::DATE)::text, 4, '0') as Year,
lpad(extract(month from event_received_timestamp::DATE)::text, 2, '0') as Month,
count(*) as play_count
from {0} 
where artist_name='Radiohead'
and end_reason_type='NATURAL_END_OF_TRACK'
and start_position_in_milliseconds='0'
and media_type='AUDIO'
group by 1,2
order by 1 asc ,2 asc 
"""