'''
Created on Jul 23, 2019

@author: latikamehra
'''


import dbOps.Postgres
import sqls.AnalyseAnomalousTrafficOverlaps
import sqls.AnalyseIndividualSpikes
import config.WikiPagesToAnalyse
from formatters import PrettyPrinter

class Analyse():
    
    def __init__(self):
        self.opWidth = 150
        self.pp = PrettyPrinter.PrettyPrint(self.opWidth)
        self.db = dbOps.Postgres.postgres(False)
        self.pages = config.WikiPagesToAnalyse.pages 
        
        self.an_overlaps_sql = sqls.AnalyseAnomalousTrafficOverlaps.sql
        self.an_indiv_sql = sqls.AnalyseIndividualSpikes.sql
        
        self.db.connect()
        
        
        
    def default_exec(self):
        self.analyseOverlappingSpikes(self.an_overlaps_sql)
        self.analyseIndividualSpikes(self.an_indiv_sql)

        self.db.closeConns()
        
        
    def analyseOverlappingSpikes(self,sql):
        res = self.db.executeReadStatement(sql)
        res = self.constructDict(res)
        self.printOverlapAnalysis(res)
        
    
    def analyseIndividualSpikes(self,sql):
        res = self.db.executeReadStatement(sql)
        res = self.constructDict(res)
        self.printIndividualSpikes(res)
        
    def printOverlapAnalysis(self, resDict):
        sep0 = "="*self.opWidth
        sep1 = "-"*self.opWidth
        
        hdr1 = "Overlapping Anomalous Traffic Data"
        hdr2 = "The following tables show dates and corresponding spike ratios for anomalous traffic data common to the set of following pages"
        
        opLines = [sep0,hdr1,hdr2,sep0]
        
        for tpl in opLines :
            self.pp.cat([tpl])
            
        for pglst in sorted(resDict.keys(), key= lambda k :len(k), reverse=True) :
            print ()
            offset = int(self.opWidth/(len(pglst)+1))
            self.pp.cat(["SPIKE RATIOS"],offset)
            
            self.pp.cat([sep1])
            
            hdrTpl = ["Date"] + list(pglst)
            self.pp.cat_tabluar(hdrTpl)
            self.pp.cat([sep1])

            pgLstDict = resDict[pglst]
            for dt in sorted(pgLstDict.keys()) :
                spikeRatios = pgLstDict[dt]
                
                prnt_spRatio = list(map(str,spikeRatios))
                prnt_row = [dt] + prnt_spRatio
                self.pp.cat_tabluar(prnt_row)

                
            self.pp.cat([sep1])  
            print ("\n\n") 
         
        print ("\n\n\n")
            
    def printIndividualSpikes(self, resDict):
        sep0 = "="*self.opWidth
        sep1 = "-"*self.opWidth
        
        hdr1 = "Individual Anomalous Traffic Data"
        hdr2 = "The following tables show dates and corresponding spike ratios for anomalous traffic data exclusive to the following pages"
        
        opLines = [sep0,hdr1,hdr2,sep0]
        
        for tpl in opLines :
            self.pp.cat([tpl])
            
        for pglst in sorted(resDict.keys(), key= lambda k : k, reverse=False) :
            print ()
            self.pp.cat([sep1])
            self.pp.cat_tabluar([pglst.upper()])
            
            self.pp.cat([sep1])
            
            hdrTpl = ["Date" , "Spike Ratio"]
            self.pp.cat_tabluar(hdrTpl)
            self.pp.cat([sep1])

            pgLstDict = resDict[pglst]
            for dt in sorted(pgLstDict.keys()) :
                spikeRatios = pgLstDict[dt]
                
                prnt_spRatio = list(str(spikeRatios))
                prnt_row = [dt] + prnt_spRatio
                self.pp.cat_tabluar(prnt_row)
                
            self.pp.cat([sep1])   
            print ("\n\n")
        
        print ("\n\n\n")

    def constructDict(self, res): # Pivots the result set for pageLists as the primary key
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
    
   
anls = Analyse()
anls.default_exec()     