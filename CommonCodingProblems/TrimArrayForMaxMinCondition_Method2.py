'''
Created on Dec 4, 2019

@author: latikamehra

Method 2 : Trim an array such that twice the minimum is greater than or equal to maximum
'''


def sortArr(arr):
    newArr = arr.copy()
    newArr.sort()
    return newArr


def isTrimmed(arr):
    minV = arr[0]
    maxV = arr[-1]
    
    if minV*2 >= maxV :
        return True
    else : 
        return False

def computeBestArr(arrList):
    sortedValidArrList = arrList.copy()
    
    sortedValidArrList.sort(key=len)  
    
    bestArr = sortedValidArrList[-1]
    
    print (bestArr)
    return (bestArr)
    
    
def computeRemovalsReqd(orgList, bestList):
    
    numRemovals = len(orgList) - len(bestList)
    print ("Number of removals required = "+str(numRemovals))
        
    

def computeBestArrayMethod_2(arr):
    orgArr = arr.copy()
    ln = len(orgArr)
    
    validArrList = [None]*ln
    
    for i in range(0,ln) :
        validArrList[i] = [orgArr[i]]
        
        for j in range(i+1, ln) :
            newArr = validArrList[i].copy()
            newArr.append(orgArr[j])
            sortedNewArr = sortArr(newArr)
            
            if isTrimmed(sortedNewArr) : 
                validArrList[i].append(orgArr[j])
            else:
                break
            
    bestArr = computeBestArr(validArrList)
    computeRemovalsReqd(orgArr, bestArr)
      
    

#orgArr = [4,5,30,12,11,10,9,200]
orgArr = [167,134,100,169,124,178,158,162,164,105,145,181,127,161,191,195,142,127,136,191,104,102,153,192,182,121,116,118,195,147,126,171,138,169,112,167,199,135,194,103,111,122,133,173,164,141,111,153,168,147,144,162,157,137,159,123,141,129,178,116,135,190,142,188,106,140,142,164,148,146,905,990,829,470,450,106,201,493,648,729,723,184,1054,856,940,1066,476,1031,408,1044,539,726,423,637,638,218,182,1029,641,933,215,739,758,804,1030,1077,406,773,486,121,845,1024,172,370,929,877,673,197,612,1086,390,261,736,455,867,755,674,131,152,450,250,1041,824,1066,530,207,291,107,437,557,387]

bestArr = computeBestArrayMethod_2(orgArr)



    

