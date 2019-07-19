'''
Created on Jul 16, 2019

@author: latikamehra
'''

class result():
    
    def __init__(self, wikiPage, anomalousActvityDict, totalNumberOfDays, totalViewCountsOfAllTime ):
        
        self.wikiPage = wikiPage
        self.anomalousActvityDict = anomalousActvityDict
        self.totalNumberOfDays = totalNumberOfDays
        self.totalViewCountsOfAllTime = totalViewCountsOfAllTime
        
    
    def prints(self):
        
        allTimeViewAvg = self.totalViewCountsOfAllTime/self.totalNumberOfDays # Calculate daily average from all the data
        
        print(("\t\t"+self.wikiPage.title()+":\n"+"#"*50+"\n\n"))
        
        print(("Total View Counts = "+ str(int(self.totalViewCountsOfAllTime)))) 
        print(("Average Daily View Count = "+ str(int(allTimeViewAvg))))
          
        print(("\n\nActivity Anomalies :\n"+"="*50))
        print(("Index\t\tDate\t\t\tViewCount\t\t\n"+"-"*50))
        
        j = 0
        for dt, vc in sorted(self.anomalousActvityDict.items()):
            j += 1    
            print((str(j)+"\t\t"+ str(dt)+"\t\t"+str(int(vc))))
            
        print(("-"*50))