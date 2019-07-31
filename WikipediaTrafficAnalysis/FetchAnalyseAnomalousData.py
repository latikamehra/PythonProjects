'''
Created on Jul 26, 2019

@author: latikamehra
'''

import logging
from execs import AnomalousTraffic
from config import WikiPagesToAnalyse
from formatters import AppLogger


nm = "FetchAnalyseAnomalousData"
AppLogger.initiate(nm, lvl=logging.INFO)
AppLogger.prntr("AnomalousResults")

at = AnomalousTraffic.FetchAnomalousTraffic(verbose=False)
at.default_exec(resetFlag=True)

anls = AnomalousTraffic.AnalyseAnomalousData()
anls.default_exec() 


