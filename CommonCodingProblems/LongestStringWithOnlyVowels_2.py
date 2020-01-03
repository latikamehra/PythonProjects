'''
Created on Dec 5, 2019

@author: latikamehra

Given a string of lower charasters, remove at most two substrings of any length from the given string such that the remaining string contains vowels('a','e','i','o','u') only.

Your aim is to maximise the length of the remaining string. Output the length of remaining string after removal of at most two substrings.

NOTE: The answer may be 0, i.e. removing the entire string.
'''


def isCharVowel(ch): 
    if ch in ['a', 'e', 'i', 'o', 'u'] : return True
    else : return False


def constrGrps(strng):
    grpArr = [""]
    
    indx = 0
    grpArr[indx] = strng[0]
    
    if isCharVowel(strng[0]) : oldType = 'v' 
    else : oldType = 'c'
      
    for i in range(1,len(strng)):
        
        if isCharVowel(strng[i]) : newType = 'v' 
        else : newType = 'c'
        
        if oldType == newType : grpArr[indx] += strng[i]
        else :
            indx += 1
            grpArr.append(strng[i])
            
        oldType = newType    
    
    #print (grpArr)        
    return grpArr
            
    
def finalAnswr(arr, vowMax):
    bestStr = ""
    startBunch = arr[0]
    endBunch = arr[-1]
    
    if isCharVowel(startBunch[0]) : startType = 'v'
    else : startType = 'c' 
    
    if isCharVowel(endBunch[0]) : endType = 'v'
    else : endType = 'c' 
    
    if startType == 'v' and endType == 'v' : bestStr = startBunch + vowMax + endBunch
    elif startType == 'c' and endType == 'c' : bestStr = vowMax
    elif startType == 'v' : bestStr = startBunch + vowMax
    else : bestStr = bestStr = vowMax + endBunch
    
    
    return bestStr
        
    
    
def maxLengthVow(arr):     
    subArr = arr[1:-1]
    maxLn = 0
    vowMax = ""
    
    for sa in subArr :
        if isCharVowel(sa[0]) :
            if len(sa) > maxLn :
                maxLn = len(sa)
                vowMax = sa
    
    #print (vowMax)            
    return vowMax


def bestString(strng):
    arr = constrGrps(strng)
    
    vowMax = maxLengthVow(arr)
    
    bestStr = finalAnswr(arr, vowMax)
    
    return bestStr
    


  
inps = ["aabbbbeee", 
        "aabbbbeeebbbb",
        "aabbbbeeebbbbiiii",
        "aabbbbeeebbbbiiiibbbb",
        "aabbbbeeebbbbiiiibbbbooooo",
        "aabbbbeeebbbbiiiibbbbooooobbbbuuuuuu",
        "bbbbaabbbbeee",
        "bbbbaabbbbeeebbbb",
        "bbbbaabbbbeeebbbbiiii",
        "bbbbaabbbbeeebbbbiiiibbbb",
        "bbbbaabbbbeeebbbbiiiibbbbooooo",
        "bbbbaabbbbeeebbbbiiiibbbbooooobbbbuuuuuu"]    

for inp in inps :
    print ("="*50)
    print ("Input String = "+inp)
    print ("-"*50)
    print (bestString(inp))
    print ("="*50+"\n\n")


