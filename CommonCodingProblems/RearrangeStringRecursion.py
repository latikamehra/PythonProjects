'''
Created on Jan 1, 2020

@author: latikamehra
Given a string str and an integer k, you need to rearrange the string in a way that the same characters must be at least k distance away. If not possible, return "".
Example1: 

Input: 

str = "aabb", k = 2

Output: 

You can return either "abab" or "baba". 

Example2: 

Input: 

str = "aaaa", k = 2

Output: 

return ""

'''
'''
def rearrangeString(strng, dist):
    
    ln = len(strng)
    
    rearrangedStringArr = [None]*ln

    charMap = {}
    
    for ch in strng :
        charMap.setdefault(ch, 0)
        charMap[ch] += 1
     
    availLen = ln 
    pntr = 0 
    charCnt = 0  
    for key, val in sorted(charMap.items(), key=lambda v : v[1], reverse=True) :
        charCnt += 1
        
        if dist*val > (availLen - 2) : 
            return ""
        
        else :
            for i in range(0,val) :
                if rearrangedStringArr[pntr] != None : 
                    rearrangedStringArr[pntr] = key
                    pntr += dist
'''


def isAdditonValid(arrStr, ch, dist):
    ln = len(arrStr)
    flag = True
    for i in range(0, ln) :
        if ch == arrStr[i] :
            if (ln - i) < dist : 
                flag = False

    return flag

def rearrStr (dist, unArrStr, arrStr = ""):  
    validStrsArr = []
    
    unArrStrArr = list(unArrStr)
    
    if len(unArrStrArr) == 0 :
        return [arrStr]  
    else :
        for i in range(0, len(unArrStrArr)) :
            ch = unArrStrArr[i]
            
            vld = isAdditonValid(arrStr, ch, dist)
            
            if vld == True :
                
                newArrStr = arrStr + ch
                newUnArrStrArr = unArrStrArr.copy()
                newUnArrStrArr.pop(i)
                
                newUnArrStr = ''.join(newUnArrStrArr)
                
                validStrs = rearrStr (dist, newUnArrStr, newArrStr)
                
                validStrsArr += validStrs
                
    return validStrsArr



k = 4
strng = "abcabcabcdefghij"


validStrs = rearrStr (k,strng)    

unqList = list(set(validStrs))

print (unqList)            
            
                           
            
            
            












































    
    