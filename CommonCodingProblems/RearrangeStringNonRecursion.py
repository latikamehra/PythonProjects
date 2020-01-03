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

def isAdditonValid(arrStr, ch, dist):
    ln = len(arrStr)
    flag = True
    for i in range(0, ln) :
        if ch == arrStr[i] :
            if (ln - i) < dist : 
                flag = False

    return flag

def rearrangeString(strng, dist):
    
    ln = len(strng)
    
    orderedCharArr = []
    rearrStr = ""
    charMap = {}
    
    for ch in strng :
        charMap.setdefault(ch, 0)
        charMap[ch] += 1
     
    unqChars = []
    
    for key, val in sorted(charMap.items(), key=lambda v : v[1], reverse=True) :
        unqChars.append(key)
        
    for uc in unqChars :
        orderedCharArr.append([uc,charMap[uc]])
        
    
    grpCnt = int(ln/dist)
    remCnt = ln%dist
    
    
    
    for i in range(0,grpCnt) :
        cntr = 0
        for j in range(0,len(unqChars)) :
            if orderedCharArr[j][1] > 0 and isAdditonValid(rearrStr, orderedCharArr[j][0], dist):
                rearrStr += orderedCharArr[j][0]
                orderedCharArr[j][1] -= 1
                cntr += 1
                
            if cntr >= dist : break
            
    
             
    cntr = 0
    for j in range(0,len(unqChars)) :
        if orderedCharArr[j][1] > 0 and isAdditonValid(rearrStr, orderedCharArr[j][0], dist):
            rearrStr += orderedCharArr[j][0]
            orderedCharArr[j][1] -= 1
            cntr += 1
            
        if cntr > remCnt : break
                
    
    if len(rearrStr) == ln :
        return rearrStr
    else :
        return ""
    


inpDct = {"abcabcabcdefghij" : 4, 
          "aabb" : 2,
          "aaaa" : 2,
          "aaabbcde" : 3,
          "aaaabb" : 2,
          "aaaaabbc" : 3}    

for strng, k in inpDct.items() :
    rearrStr = rearrangeString(strng, k)
    
    print ("="*50)
    print ("Distance = "+str(k))
    print ("Original String = \t\t" + strng)
    print ("-"*50)
    print ("Rearranged String = \t\t"+rearrStr)
    print ("="*50 + "\n\n")
                           
            
            
            












































    
    