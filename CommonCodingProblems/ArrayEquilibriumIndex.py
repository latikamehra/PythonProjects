def sumArr(arr):
    sm = 0
    for a in arr :
        sm += a 
    return sm

def solution(arr):
    
    ln = len(arr)
    possPs = []
    
    for p in range(0, ln) :
        leftArr = arr[0:p]
        rightArr = arr[p+1:]

        if sumArr(leftArr) == sumArr(rightArr) :
            possPs.append(p) 
        
    return possPs 

lst = [-1,3,-4,5,1,-6,2,1]
print (solution(lst))
        