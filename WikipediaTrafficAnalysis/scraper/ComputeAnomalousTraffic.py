'''
Created on Jul 16, 2019

@author: latikamehra
'''

from dataStructures import AnomalousTraffic
from . import GetTrafficData


class AnomalousDays():
    
    def __init__(self, lastnDays, thresholdFactor):
        self.lastnDays = lastnDays
        self.thresholdFactor = thresholdFactor
        

    def get(self, wikiPageFor):
           
        pgvw = GetTrafficData.pageview() # Create an object to get Wiki details
        
        viewMap =  pgvw.getPerDayViews(wikiPageFor) # Fetch the dictionary containing daily page views
        
        lstOfTpls = sorted(viewMap.items()) # Sort the dictionary into a list of tuples
        
        lstlen = len(lstOfTpls)
        
        anomalousActvityDays = {}
        
        runningAvgOflastnDays = 0
        
        totalViewCountsOfAllTime = 0
        
        for i in range(lstlen) :
            dt = lstOfTpls[i][0]
            vc = float(lstOfTpls[i][1])
            
            totalViewCountsOfAllTime += vc # Add cureent view count to total
            
            #print vc
            
            if i<self.lastnDays :
                
                runningAvgOflastnDays = (runningAvgOflastnDays*i + vc)/float(i+1) # New Running Average of the last "i" number of days
                
            else:
                
                if (vc > runningAvgOflastnDays*self.thresholdFactor) :  # If the current view count is greater than running average times the threshold factor then the day was anomalous
                    anomalousActvityDays[dt.strftime("%Y-%m-%d")] = vc
                    
                
                vc_nDaysAgo = float(lstOfTpls[i-self.lastnDays][1])
                runningAvgOflastnDays = (runningAvgOflastnDays*self.lastnDays - vc_nDaysAgo + vc)/float(self.lastnDays) # New Running Average of the last "n" number of days
                
                #print "New Running Average of last "+str(n)+" days : "+str(runningAvgOfself.lastnDays)
                
        
        res = AnomalousTraffic.result(wikiPageFor, anomalousActvityDays, lstlen, totalViewCountsOfAllTime) # Create result object for the WikiPage
        #res.prints()
        
        return res
            


