'''
Created on Dec 4, 2019

@author: latikamehra

Method 1 : Trim an array such that twice the minimum is greater than or equal to maximum
'''


def sortArr(arr):
    newArr = arr.copy()
    newArr.sort()
    return newArr


def validMinMax(arr):
    dicts = {}
    sz = len(arr)
    
    for i in range(0,sz) :
        dicts[arr[i]] = None
        for j in range(sz-1, i, -1) :
            if arr[i]*2 >= arr[j] :
                dicts[arr[i]] = arr[j]
                break
            
    return dicts

def computeBestArr(arrList):
    sortedValidArrList = arrList.copy()
    
    sortedValidArrList.sort(key=len)  
    
    bestArr = sortedValidArrList[-1]
    
    print (bestArr)
    return (bestArr)
    
    
def computeRemovalsReqd(orgList, bestList):
    
    numRemovals = len(orgList) - len(bestList)
    print ("Number of removals required = "+str(numRemovals))
    
    

def computeBestArrayMethod_1(arr):
    orgArr = arr.copy()
    ln = len(orgArr)
    sortedArr = sortArr(arr)
    
    validMinMaxPairs = validMinMax(sortedArr)
    
    #print(validMinMaxPairs)

    validArrList = [None]*ln
    
    for i in range(0,ln) :
        minV = maxV = orgArr[i]
        validArrList[i] = [orgArr[i]]
        for j in range(i+1, ln) :
            if orgArr[j] >= maxV : maxV = orgArr[j]
            if orgArr[j] <= minV : minV = orgArr[j]
            
            if validMinMaxPairs[minV] is not None :
                if validMinMaxPairs[minV] >= maxV :
                    validArrList[i].append(orgArr[j])
                else :
                    break
    
    bestArr = computeBestArr(validArrList)
    computeRemovalsReqd(orgArr, bestArr)
    

#orgArr = [4,5,30,12,11,10,9,200]
orgArr = [167,134,100,169,124,178,158,162,164,105,145,181,127,161,191,195,142,127,136,191,104,102,153,192,182,121,116,118,195,147,126,171,138,169,112,167,199,135,194,103,111,122,133,173,164,141,111,153,168,147,144,162,157,137,159,123,141,129,178,116,135,190,142,188,106,140,142,164,148,146,905,990,829,470,450,106,201,493,648,729,723,184,1054,856,940,1066,476,1031,408,1044,539,726,423,637,638,218,182,1029,641,933,215,739,758,804,1030,1077,406,773,486,121,845,1024,172,370,929,877,673,197,612,1086,390,261,736,455,867,755,674,131,152,450,250,1041,824,1066,530,207,291,107,437,557,387]

bestArr = computeBestArrayMethod_1(orgArr)



    

