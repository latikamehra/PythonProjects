'''
Created on Dec 5, 2019

@author: latikamehra

Given a two 2D integer array, find the max score of a path from the upper left cell to bottom right cell. The score of a path is the minimum value in that path.
Moving only right & down
'''


def findPossPaths(d, r):
    pathSet = []
    if d == 0 and r == 0 :
        return []
    elif d == 0 :
        return ["R"*r]
    elif r == 0 :
        return ["D"*d]
    else :
        pathSetDown = []
        pathSetRight = []
        
        downPathArr = findPossPaths(d-1, r)
        rightPathArr = findPossPaths(d, r-1)
        
        for dd in downPathArr :
            pathSetDown.append("D"+dd)
            
        for rr in rightPathArr :
            pathSetRight.append("R"+rr)

        pathSet = pathSetDown + pathSetRight
        
    return pathSet


def findMinOnPath(arrArr, path):
    
    minV = arrArr[0][0]
    r = 0
    c = 0
    
    for step in path : 
        if step == 'R' : c = c+1
        if step == 'D' : r = r+1
        
        newElem = arrArr[r][c]
        
        if newElem < minV : minV = newElem

    print ("Minimum on path "+ path + " is "+str(minV))
    return minV
        
         

def maxPathScore(arrArr):
    # Rows are the internal arrays, such that (r,c) element = arrArr[r][c]
    # Assuming arrArr is rxc is size
    
    numRows = len(arrArr)
    
    numCols = len(arrArr[0])
    
    pathSets = findPossPaths(numRows-1, numCols-1) # Number of Rights & Lefts would be 1 less than Col & Row counts respectively
    
    maxOfMins = findMinOnPath(arrArr, pathSets[0])
    
    for path in pathSets :
        
        minOfPath = findMinOnPath(arrArr, path)
        
        if minOfPath > maxOfMins : maxOfMins = minOfPath
        
        
    return maxOfMins
        
    
arrArr = [[7,5,3], [2,0,9], [4,5,9]]

print (maxPathScore(arrArr))
    