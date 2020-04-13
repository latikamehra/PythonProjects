'''
Created on Jan 8, 2020

@author: latikamehra

Check if two binary encoded numbers are consecutive in Gray code
'''

def insertionSort(unsortedArr):
    sortedArr=[unsortedArr[0]]
    
    for i in range(1,len(unsortedArr)) :
        for j in range(0,len(sortedArr)) :
            insertedFlag = False
            if sortedArr[j] > unsortedArr[i] :
                sortedArr.insert(j,unsortedArr[i])
                insertedFlag = True
                break
        if not insertedFlag : sortedArr.append(unsortedArr[i])
            
    return sortedArr        
            
arr = [5,8,1,4,9,4,2,7,3,6]
print(insertionSort(arr))



        
    