def bringMaxToFront(arr,maxArrVal, maxArrInd) :
    arrCopy = arr.copy() 
    
    firstVal = arrCopy[0]

    arrCopy[0] = maxArrVal
    arrCopy[maxArrInd] = firstVal

    return arrCopy


def minimumSwaps(popularity):
    # Write your code here
    swaps = 0

    for i in range(0, len(popularity)):
        subArr = popularity[i:]

        maxArrVal = max(subArr)
        maxArrInd = subArr.index(maxArrVal)

        if maxArrInd !=0 :
            swaps += 1
            newSubArr = bringMaxToFront(subArr,maxArrVal,maxArrInd)
            popularity = popularity[:i] + newSubArr

    return swaps