'''
Created on Aug 7, 2019

@author: latikamehra
'''

sql = """select replace(content_name, ' (Remastered)', '') as song, 
count(*) as play_count
from {0}  
where artist_name='Radiohead'
and end_reason_type='NATURAL_END_OF_TRACK'
and start_position_in_milliseconds='0'
and media_type='AUDIO'
group by 1
order by 2 desc
"""