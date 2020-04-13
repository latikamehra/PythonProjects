'''
Created on Jan 8, 2020

@author: latikamehra

Check if two binary encoded numbers are consecutive in Gray code
'''

def bubbleSort(unsortedArr):
    ln = len(unsortedArr)
    
    
    for j in range(ln-1, 1, -1) :
        for i in range(0, j) :
            if unsortedArr[i] > unsortedArr[i+1] :
                tmp = unsortedArr[i]
                unsortedArr[i] =  unsortedArr[i+1]
                unsortedArr[i+1] = tmp
                
    return unsortedArr   
            
arr = [5,8,1,4,9,4,2,7,3,6]
print(bubbleSort(arr))


        
    