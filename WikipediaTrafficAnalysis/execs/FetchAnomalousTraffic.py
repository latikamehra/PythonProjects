'''
Created on Jul 16, 2019

@author: latikamehra
'''


from scraper import ComputeAnomalousTraffic
from dbOps import Postgres


res = {}
lastnDays = 10 # Last 'n' number of days to consider for average
thresholdFactor = 2 # Acceptable ratio between current view count & running average
ad = ComputeAnomalousTraffic.AnomalousDays(lastnDays, thresholdFactor)

wikiPages = ["jonny greenwood", "radiohead", "thom yorke"]

for wikipg in wikiPages :
    res[wikipg] = ad.get(wikipg)
    res[wikipg].prints()
    print("\n\n\n")

