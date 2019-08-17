'''
Created on Aug 7, 2019

@author: latikamehra
'''

sql = """WITH 
plcnt as 
(select replace(content_name, ' (Remastered)', '') as song,
lpad(extract(year from event_received_timestamp::DATE)::text, 4, '0') as year,
lpad(extract(month from event_received_timestamp::DATE)::text, 2, '0') as month,
count(*) as play_count
from {0} 
where artist_name='Radiohead'
and end_reason_type='NATURAL_END_OF_TRACK'
and start_position_in_milliseconds='0'
and media_type='AUDIO'
group by 1,2,3),

rnkr as
(select song, concat(year,'-',month) as yrmnth, play_count,
rank() over (partition by year, month order by play_count desc, song asc) as rnk
from plcnt)

select yrmnth, song, play_count 
from rnkr 
where rnk<={1} 
order by 1 asc,3 desc, 2 asc
"""