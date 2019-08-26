'''
Created on Aug 26, 2019

@author: latikamehra
'''


from manageDuplicates import DuplicatesForReview

class Review :
    
    def __init__(self, obj):
        self.DictBckp = obj.DictBckp
        self.RvwdBckp = obj.RvwdBckp
        
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
                
            self.printReviewInfo()
            
        else :
            print("No probable duplicate files found in the directory.\nSkipping")
            #quit()
            
            
    def printReviewInfo(self):
        '''
        prntStr = ""
        prntStr += "\n\n"
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat(["List of reviewed duplicates"])
        prntStr += self.pp.cat([self.sep1])
        prntStr += self.pp.cat([self.pp.collectionPrnt(self.reviewedDupeDict)])
        self.op_summary.info(prntStr)
        '''
        self.RvwdBckp.writeDict(self.reviewedDupeDict)
        
        
