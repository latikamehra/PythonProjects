
def arrayRotate(a,rotate):    
    lena = len(a)
    maxOfA = max(a) 
    maxOfA_stInd = a.index(maxOfA)

    indicesResult = [None]*len(rotate)
 
    for j in range(0, len(rotate)) :
        turn = rotate[j]
        effectiveTurn = rotate[j]
        this_maxOfA_stInd = maxOfA_stInd - turn 

        if this_maxOfA_stInd < 0 :
            this_maxOfA_stInd =  this_maxOfA_stInd%lena

        indicesResult[j] = this_maxOfA_stInd 

    return indicesResult
