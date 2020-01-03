'''
Created on Jan 1, 2020

@author: latikamehra

Implement the following class to keep track of the first unique number in a data stream... 

eg :
stream.getFirstUniqueNum() --> None
stream.add(10)
stream.getFirstUniqueNum() --> 10
stream.add(11)
stream.getFirstUniqueNum() --> 10
stream.add(10)
stream.getFirstUniqueNum() --> 11
'''


class DataStream :
    
    def __init__(self):
        self.arr = []
        self.arrMap = {}
        self.continueFlag = True
        

    def addToStream(self):
        print ("Input a number to the stream else press Enter")
        ip = input()
        
        if ip != "":
            self.arrMap.setdefault(ip, 0)
            self.arrMap[ip] += 1
            
            if ip not in self.arr : self.arr.append(ip)

        else :
            self.continueFlag = False
        
        
    def getFirstUnq(self):
        for el in self.arr :
            if self.arrMap[el] == 1 : 
                print ("First Unique number in the steam is : "+str(el))
                return
            
        print ("First Unique number in the steam is : None")

    
    
ds = DataStream()

while (ds.continueFlag) :
    ds.getFirstUnq()
    ds.addToStream()
    


        
            

        
    
        
    
