'''
Created on Aug 26, 2019

@author: latikamehra
'''


from manageDuplicates import DuplicatesForReview

class Review :
    
    def __init__(self, obj):
        self.DictBckp = obj.DictBckp
        self.RvwdBckp = obj.RvwdBckp
        
        self.reviewedDupeDict = {}
        
        self.pp = obj.pp
        self.sep1 = obj.sep1
        
        self.op_summary = obj.op_summary
        
        self.getDupeCount = obj.getDupeCount

        
    
    def review(self, manualReview):
        probDict = self.DictBckp.readDict()
        
        if len(probDict) >= 1 :
        
            dplct = DuplicatesForReview.Review()
            
            if manualReview == True :
                self.reviewedDupeDict = dplct.reviewDuplicates(probDict)
            else :
                self.reviewedDupeDict = probDict
            
        else :
            print("No probable duplicate files found in the directory.\nSkipping")
            #quit()
        
        self.printReviewInfo()    
            
    def printReviewInfo(self):
        self.RvwdBckp.writeDict(self.reviewedDupeDict)
        
        
