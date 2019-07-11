'''
Created on Jul 11, 2019

@author: latikamehra
'''

import PageviewCountsFromWikipedia
import datetime





class AnomalousDays():
        

    def get(self, wikiPageFor, countForAvgDays, threshold):
    
        pgvw = PageviewCountsFromWikipedia.pageview()
        
        viewMap =  pgvw.getPerDayViews(wikiPageFor)
        
        lstOfTpls = sorted(viewMap.items())
        
        lstlen = len(lstOfTpls)
        
        anomalousActvityDays = {}
        
        runningAvgOfLastnDays = 0
        
        for i in range(lstlen) :
            dt = lstOfTpls[i][0]
            vc = float(lstOfTpls[i][1])
            
            #print vc
            
            if i<countForAvgDays :
                
                runningAvgOfLastnDays = (runningAvgOfLastnDays*i + vc)/float(i+1) # New Running Average
                
            else:
                
                if (vc > runningAvgOfLastnDays*threshold) :
                    anomalousActvityDays[dt.strftime("%Y-%m-%d")] = vc
                    
                
                vc_nDaysAgo = float(lstOfTpls[i-countForAvgDays][1])
                runningAvgOfLastnDays = (runningAvgOfLastnDays*countForAvgDays - vc_nDaysAgo + vc)/float(countForAvgDays) # New Running Average
                
                #print "New Running Average of last "+str(n)+" days : "+str(runningAvgOfLastnDays)
                
            
        print "Activity Anomalies :\n"+"="*50
        print "Date\t\t\tViewCount\t\t\n"+"-"*50
        
        for dt, vc in sorted(anomalousActvityDays.items()):
                
            print str(dt)+"\t\t"+str(vc)
            
            
            
            
            
            
            
            

wikiPageFor = "jonny greenwood"
countForAvgDays = 10 # Last 'n' number of days to consider for average
threshold = 2 # Acceptable ratio between current view count & running average
ad = AnomalousDays()
ad.get(wikiPageFor, countForAvgDays, threshold)