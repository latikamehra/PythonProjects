def solution(arr):
    ln = len(arr)
    
    midIndx = ln//2
    candidate = arr[midIndx]
    counter = 0
    
    for i in range(0,len(arr)) :
        if arr[i] == candidate : counter += 1
        
    if counter*2 > len(arr) :
        return candidate 
    else :
        return -1
    
        