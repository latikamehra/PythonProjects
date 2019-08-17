'''
Created on Jul 16, 2019

@author: latikamehra
'''


from scraper import ComputeAnomalousTraffic
import config.AnomalousTraffic
import dbOps.AnomalousTraffic
import config.WikiPagesToAnalyse

import dbOps.Postgres
from sqls import AnalyseAnomalousTrafficOverlaps, AnalyseIndividualSpikes, AverageTrafficRatios
from formatters import PrettyPrinter, AppLogger


class FetchAnomalousTraffic():
    
    def __init__(self, verbose=False):
        self.log = AppLogger.logger.getChild(__name__)
        self.op = AppLogger.op
        self.db = dbOps.AnomalousTraffic.dbOps(verbose)
        self.pages = config.WikiPagesToAnalyse.pages 
        
    
    def default_exec(self, resetFlag=False):
        rslt = self.fetch(self.pages)
        self.write(rslt, resetFlag)
        self.db.closeDBConnections()
        
        

    def fetch(self,wikiPages):
        res = {}
        ad = ComputeAnomalousTraffic.AnomalousDays(config.AnomalousTraffic.lastnDays, config.AnomalousTraffic.thresholdFactor)
        
        for wikipg in wikiPages :
            try :
                res[wikipg] = ad.get(wikipg)
            except Exception as e:
                #self.log.error(e)
                continue
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
            
       
  
class AnalyseAnomalousData():
    
    def __init__(self):
        
        self.op = AppLogger.op
        
        self.db = dbOps.Postgres.postgres(False)
        self.pages = config.WikiPagesToAnalyse.pages 
        
        self.trafficRatios_sql = AverageTrafficRatios.sql
        self.an_overlaps_sql = AnalyseAnomalousTrafficOverlaps.sql
        self.an_indiv_sql = AnalyseIndividualSpikes.sql
        
        self.opWidth = self.computeOpWidth(self.pages)
        self.pp = PrettyPrinter.PrettyPrint(self.opWidth)
        self.sep0 = "="*self.opWidth
        self.sep1 = "-"*self.opWidth
        
        self.db.connect()
        
    def computeOpWidth(self, pages):
        minColLen = max(map(len,pages)) # Compute length of the longest Page KeyWord
        ln = (minColLen+3)*(len(pages)+1) # Add 3 to that required minimum column length for pipe and space, multiply by number of columns + 1 for the possible column of "Date"
        
        opWidth = max(120,ln) # Output width should be either equal to ln computed above or atleast 150 characters long
        return (opWidth)
            
        
    def getAllAnalyses(self):
        self.trafficRatios()
        self.analyseOverlappingSpikes()
        self.analyseIndividualSpikes()

        self.db.closeConns()
    
    def trafficRatios(self):
        res = self.db.executeReadStatement(self.trafficRatios_sql)
        self.printTrafficRatios(res)
        
    def analyseOverlappingSpikes(self):
        res = self.db.executeReadStatement(self.an_overlaps_sql)
        res = self.constructDict(res)
        self.printOverlapAnalysis(res)
        
    
    def analyseIndividualSpikes(self):
        res = self.db.executeReadStatement(self.an_indiv_sql)
        res = self.constructDict(res)
        self.printIndividualSpikes(res)
        
    def printOverlapAnalysis(self, resDict):
        
        
        hdr1 = "Overlapping Anomalous Traffic Data"
        hdr2 = "The following tables show dates and corresponding spike ratios for anomalous traffic data common to the set of following pages"
        
        opLines = [self.sep0,hdr1,hdr2,self.sep0]
        
        for tpl in opLines :
            self.op.info(self.pp.cat([tpl]))
            
        for pglst in sorted(resDict.keys(), key= lambda k :len(k), reverse=True) :
            self.op.info("")
            offset = int(self.pp.opWidth/(len(pglst)+1))
            self.op.info(self.pp.cat(["SPIKE RATIOS"],offset))
            
            self.op.info(self.pp.cat([self.sep1]))
                         
            hdrTpl = ["Date"] + list(pglst)
            self.op.info(self.pp.cat_tabluar(hdrTpl))
            self.op.info(self.pp.cat([self.sep1]))

            pgLstDict = resDict[pglst]
            for dt in sorted(pgLstDict.keys()) :
                spikeRatios = pgLstDict[dt]
                
                prnt_spRatio = list(map(str,spikeRatios))
                prnt_row = [dt] + prnt_spRatio
                self.op.info(self.pp.cat_tabluar(prnt_row))

                
            self.op.info(self.pp.cat([self.sep1]))  
            self.op.info("\n\n") 
         
        self.op.info("\n\n\n")
            
    def printIndividualSpikes(self, resDict):
        
        hdr1 = "Individual Anomalous Traffic Data"
        hdr2 = "The following tables show dates and corresponding spike ratios for anomalous traffic data exclusive to the following pages"
        
        opLines = [self.sep0,hdr1,hdr2,self.sep0]
        
        for tpl in opLines :
            self.op.info(self.pp.cat([tpl]))
            
        for pglst in sorted(resDict.keys(), key= lambda k : k, reverse=False) :
            self.op.info("")
            self.op.info(self.pp.cat([self.sep1]))
            self.op.info(self.pp.cat_tabluar([pglst.upper()]))
            
            self.op.info(self.pp.cat([self.sep1]))
            
            hdrTpl = ["Date" , "Spike Ratio"]
            self.op.info(self.pp.cat_tabluar(hdrTpl))
            self.op.info(self.pp.cat([self.sep1]))

            pgLstDict = resDict[pglst]
            for dt in sorted(pgLstDict.keys()) :
                spikeRatios = pgLstDict[dt]
                
                prnt_spRatio = [str(spikeRatios)]
                prnt_row = [dt] + prnt_spRatio
                self.op.info(self.pp.cat_tabluar(prnt_row))
                
            self.op.info(self.pp.cat([self.sep1]))   
            self.op.info("\n\n")
        
        self.op.info("\n\n\n")
        
        
    def printTrafficRatios(self,resLst):

        
        hdr1 = "Daily Average Traffic Ratios"
        hdr2 = "The following pages have their average daily view counts in the following ratios to one another"
        
        opLines = [self.sep0,hdr1,hdr2,self.sep0]
        
        for tpl in opLines :
            self.op.info(self.pp.cat([tpl]))
         
        pg = []
        ratio = []    
        for tpl in resLst :
            pg.append(tpl[0])
            ratio.append(str(tpl[1]))
            
        
        self.op.info(self.pp.cat([self.sep1]))
        self.op.info(self.pp.cat_tabluar(pg))
        self.op.info(self.pp.cat([self.sep1]))
        self.op.info(self.pp.cat_tabluar(ratio))
        self.op.info(self.pp.cat([self.sep1]))   
        
        self.op.info("\n\n\n")

    def constructDict(self, res): # Pivots the result set for pageLists as the primary key
        #print (res)
        pagesDict = {}
        for row in res :
            dateSpikeDict = {}
            
            date = row[0]
            if len(row[1])>1 :
                orderedPages = tuple(row[1])
                orderedsSpikeFactors = tuple(row[2])
            else:
                orderedPages = row[1][0]
                orderedsSpikeFactors = row[2][0]
            
            dateSpikeDict[date] = orderedsSpikeFactors
            
            if orderedPages not in pagesDict.keys() : # If the set of wiki pages does NOT already exist in the final dictionary initiate it and then add the new date+spikeFactorList dictionary to its values
                pagesDict[orderedPages] = {}
                               
            pagesDict[orderedPages].update(dateSpikeDict)
                
        return(pagesDict)  
    

if __name__ == '__main__' :
    f = FetchAnomalousTraffic(True)
    f.default_exec(True)
    
    a = AnalyseAnomalousData()
    a.default_exec()
    
    
