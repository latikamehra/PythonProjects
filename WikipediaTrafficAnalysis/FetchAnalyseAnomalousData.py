'''
Created on Jul 26, 2019

@author: latikamehra
'''

from execs import AnomalousTraffic
import logging

nm = "FetchAnalyseAnomalousData"
lev = logging.WARNING

logging.basicConfig(filename='logs/'+nm+'.log',level=lev, filemode='w', format='[%(levelname)s] => %(name)s : \n\t%(message)s \n')

at = AnomalousTraffic.FetchAnomalousTraffic(verbose=False)
at.default_exec(resetFlag=True)

anls = AnomalousTraffic.AnalyseAnomalousData()
anls.default_exec() 


