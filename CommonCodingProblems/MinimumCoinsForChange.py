'''
Created on Dec 5, 2019

@author: latikamehra
V = number of cents that need to be returned for change
C = [C1, C2, ... Cm] Array of coins that you have an infinite supply of with various denominations
Find minimum number of coins required for making the change
'''

def minLenArr(arr):
    newArr = arr.copy()
    newArr.sort(key=len)
    return (newArr[0])


def sumArr(arr):
    sm = 0
    for it in arr :
        sm += it
        
    return sm


def minCombsRecr(V, C):
    possArrList = []
    combSz = 0
    
    if V == 0 :
        return []
    
    for i in range(0, len(C)) :
        possArr = []
        if C[i] == V : 
            return([C[i]])
        elif C[i] < V :
            possArr.append(C[i])
            subComb = minCombsRecr(V-C[i], C)
            if subComb != None :
                possArr = possArr + subComb
                possArrList.append(possArr)
            else :
                return None
            
     
    #print (possArrList)    
    return minLenArr(possArrList)

        
                
    
    
    
C = [9,6,5,1,11]
V = 11

print (minCombsRecr(V,C))