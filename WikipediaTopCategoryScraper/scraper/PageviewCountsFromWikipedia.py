'''
Created on Jul 10, 2019

@author: latikamehra
'''

import requests
import json
import datetime
from datetime import date

class pageview() :
    
    def __init__(self):
        self.base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"
    
        self.startDt = self.getStartEndDates(4)[0]
        self.endDt = self.getStartEndDates(4)[1]
        
    
    def getStartEndDates(self, duration):
        now = date.today()
        
        eyear = now.strftime("%Y")
        emonth = now.strftime("%m")
        eday = now.strftime("%d")
        
        syear = str(int(eyear) - duration)
        smonth = emonth
        sday = "01"
        
        startDt = syear+smonth+sday+"00"
        endDt = eyear+emonth+eday+"00"
        
        return startDt,endDt
    
    
    def formatWikiDate(self, dt):
        yr = dt[0:4]
        mnth = dt[4:6]
        day = dt[6:8]
        
        frmdt = datetime.datetime(int(yr), int(mnth), int(day))
        
        return frmdt
        
        
    
    def getPerDayViews(self, keywrd):
        jaslist = self.getWikiResponse(keywrd)
        viewMap = {}
        
        for entry in jaslist :
            view = entry["views"]
            dt = entry["timestamp"]
            frmdt = self.formatWikiDate(dt)
            
            viewMap[frmdt] = view
            
        return viewMap
        
  
    def getTotalViewCount(self, keywrd):
        totalViews = 0
        
        jaslist = self.getWikiResponse(keywrd)
        
        for entry in jaslist :
            view = entry["views"]
            totalViews += view
                
        
        return totalViews
    
    
    def getWikiResponse(self, keywrd):
        keywrd = keywrd.title().replace(" ", "_")
        
        self.wikiurl = self.base_url.format(keywrd,self.startDt,self.endDt)
        
        #print self.wikiurl
        
        response = requests.get(self.wikiurl)
        cont = response.content
        parsed = json.loads(cont)
        jlist = parsed["items"]
        
        return jlist