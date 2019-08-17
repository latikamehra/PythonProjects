'''
Created on Jul 26, 2019

@author: latikamehra
'''

import logging
from execs import AnomalousTraffic
from formatters import AppLogger
import datetime

curTime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
debugLog = "FetchAnalyseAnomalousData_"+curTime
opFile = "AnomalousResults_"+curTime
level = logging.INFO

AppLogger.initiate(debugLog, lvl=level)
AppLogger.prntr(opFile)

at = AnomalousTraffic.FetchAnomalousTraffic(verbose=False)
at.default_exec(resetFlag=True)

anls = AnomalousTraffic.AnalyseAnomalousData()
anls.trafficRatios() 


