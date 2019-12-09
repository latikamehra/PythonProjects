'''
Created on Dec 5, 2019

@author: latikamehra

Given a string of lower charasters, remove at most two substrings of any length from the given string such that the remaining string contains vowels('a','e','i','o','u') only.

Your aim is to maximise the length of the remaining string. Output the length of remaining string after removal of at most two substrings.

NOTE: The answer may be 0, i.e. removing the entire string.
'''

import re 

def splitString(str):
    vowelBunches = re.findall(r'([aeiou]+)', str)
    
    consonantBunches = re.findall(r'([b-df-hj-np-tv-xz]+)', str)
    
    return vowelBunches, consonantBunches
    
    
def constrCollArr(vowelBunches, consonantBunches):
    collectiveArr = []
    if checkConsVow(str[0]) == "v" : 
        firstArr = vowelBunches.copy()
        secondArr = consonantBunches.copy()
    else :
        secondArr = vowelBunches.copy()
        firstArr = consonantBunches.copy()
        
    maxLen = min(len(vowelBunches), len(consonantBunches))
    
    for i in range(0, maxLen) :
        
        if len(firstArr) == maxLen : collectiveArr.append(firstArr[i])
        if len(secondArr) == maxLen : collectiveArr.append(secondArr[i])
        
       
    return collectiveArr

def checkConsVow(str):
    if str[0] in ['a', 'e', 'i', 'o', 'u'] :
        return "v"
    else :
        return "c"
    

def findMaxVowelSets(vArr):
    tempArr = vArr.copy()
    tempArr.sort(reverse=True,key=len)
    return (tempArr[0], vArr.index(tempArr[0]))

def handleAsymmetricSituation(vArr, index):
    remVarr = vArr.copy()
    remVarr.pop(index)
    
    max1, index2 =  findMaxVowelSets(remVarr) 
    if index < index2 :
        finTrimmedWord = vArr[index]+remVarr[index2]
    else:
        finTrimmedWord = remVarr[index2]+vArr[index]
        
    return finTrimmedWord  
            
    
def findMaxTrimmed(str):  
    finTrimmedWord = ""
    vArr , cArr = splitString(str)
    
    if len(vArr) == 0 :
        finTrimmedWord = ""
        return finTrimmedWord
    elif len(vArr) == 1 :
        finTrimmedWord = vArr[0]
        return finTrimmedWord
    elif len(cArr) < 3 :
        for vb in vArr :
            finTrimmedWord += vb
        return finTrimmedWord
    else :
        if checkConsVow(str[0]) == "c" and checkConsVow(str[-1]) == "c" : # Check if the original string starts and ends with at least a consonant
            finTrimmedWord, ind =  findMaxVowelSets(vArr) # In this case only one vowel set can be kept
            return finTrimmedWord
        elif checkConsVow(str[0]) == "v" and checkConsVow(str[-1]) == "v" :
            max1, ind =  findMaxVowelSets(vArr)
            remVarr = vArr.copy()
            if len(vArr[0]) >= len(vArr[-1]) : 
                endVB = vArr[0]
                remVarr.pop(0)
                max1, ind =  findMaxVowelSets(remVarr) 
                finTrimmedWord = endVB+max1
            else:
                endVB = vArr[-1]
                remVarr.pop()
                max1, ind =  findMaxVowelSets(remVarr) 
                finTrimmedWord = max1+endVB
            
            
            return finTrimmedWord
        
        elif  checkConsVow(str[0]) == "c" and checkConsVow(str[-1]) == "v" :
            finTrimmedWord = handleAsymmetricSituation(vArr, -1)
            return finTrimmedWord
        else :
            finTrimmedWord = handleAsymmetricSituation(vArr, 0)
            return finTrimmedWord
            
            

    
    
print (findMaxTrimmed("aaaaqqeeeqqiiiiiqquuqq"))
print (findMaxTrimmed("letsgosomewhere"))




