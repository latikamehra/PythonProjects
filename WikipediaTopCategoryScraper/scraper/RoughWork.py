'''
Created on Jul 10, 2019

@author: latikamehra
'''

'''

# Get PageCounts for a page with keyword

import PageviewCountsFromWikipedia

pgvw = PageviewCountsFromWikipedia.pageview()

print pgvw.getTotalViewCount("jonny greenwood")

'''


#'''

# Get Daily PageCounts for a page with keyword

import PageviewCountsFromWikipedia
import datetime

pgvw = PageviewCountsFromWikipedia.pageview()

viewMap =  pgvw.getPerDayViews("jonny greenwood")

lstOfTpls = sorted(viewMap.items())

lstlen = len(lstOfTpls)

anomalousActvityDays = {}

n = 5 # Last 'n' number of days to consider for average
factor = 2 # Acceptable ratio between current view count & running average

runningAvgOfLastnDays = 0

for i in range(lstlen) :
    dt = lstOfTpls[i][0]
    vc = float(lstOfTpls[i][1])
    
    #print vc
    
    if i<n :
        
        runningAvgOfLastnDays = (runningAvgOfLastnDays*i + vc)/float(i+1) # New Running Average
        
    else:
        
        if (vc > runningAvgOfLastnDays*factor) :
            anomalousActvityDays[dt.strftime("%Y-%m-%d")] = vc
            
        
        vc_nDaysAgo = float(lstOfTpls[i-n][1])
        runningAvgOfLastnDays = (runningAvgOfLastnDays*n - vc_nDaysAgo + vc)/float(n) # New Running Average
        
        #print "New Running Average of last "+str(n)+" days : "+str(runningAvgOfLastnDays)
        
    
print "Days with anomalous view counts :"

for dt, vc in sorted(anomalousActvityDays.items()):
        
    print str(dt)+" : "+str(vc)
    
        

#print lstOfTpls[-1][1]

#'''

