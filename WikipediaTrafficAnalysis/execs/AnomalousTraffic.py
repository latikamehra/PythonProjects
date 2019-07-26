'''
Created on Jul 16, 2019

@author: latikamehra
'''


from scraper import ComputeAnomalousTraffic
import config.AnomalousTraffic
import dbOps.AnomalousTraffic
import config.WikiPagesToAnalyse


class AnomalousTraffic():
    
    def __init__(self, verbose):
        self.db = dbOps.AnomalousTraffic.dbOps(verbose)
        self.pages = config.WikiPagesToAnalyse.pages 
        
    
    def default_exec(self, resetFlag):
        rslt = self.fetch(self.pages)
        self.write(rslt, resetFlag)
        self.read()

        self.db.closeDBConnections()
        
        

    def fetch(self,wikiPages):
        res = {}
        ad = ComputeAnomalousTraffic.AnomalousDays(config.AnomalousTraffic.lastnDays, config.AnomalousTraffic.thresholdFactor)
        
        for wikipg in wikiPages :
            res[wikipg] = ad.get(wikipg)
            
        return res
            
        
    def write(self,resData, reset):
        if reset == True:
            self.db.resetTables()
            
        for res in resData.values() :
            self.db.writeData(res)
        
        
    def read(self):    
        for wikipg in self.pages :
            print(self.db.readPageTotalData(wikipg))
            print(self.db.readAnomalousData(wikipg))
            
        
    
    
    
at = AnomalousTraffic(False)
at.default_exec(True)