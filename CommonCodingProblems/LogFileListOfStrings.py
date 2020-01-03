'''
Created on Dec 10, 2019

@author: latikamehra

You have been given a task of recording some data 40M a log file. In the log file, every line is a space-delimited list of strings. All lines begin with an alphanumeric identifier. There will be no lines consisting only of an identifier.
After the alphanumeric identifier a line will consist of either:
- a list of words using only lowercase English letters
- or list of only integers.
You have to reorder the data such that all of the lines with words are at the top of the log file. The lines with words are ordered lexicographically. ignoring the identifier except in the case of ties In the case of ties (if there are two lines that are identical except for the identifier) the identifier is used to order lexicographically. Alphanumeric should be sorted in ASCII order (numbers come before letters) The identifiers most still be pan of the lines in the output Strings. Lines with integers must be left in the original order they were in the file.
Write an algorithm to reorder the data in the log file, according to the rules above.
Input
The input to the function/method consists of two argument - logFileSize, an integer representing the number of log lines.
logLines, a list of strings representing the log file.


Output
Return a list of strings representing the reordered log file data

Note
Identifier consists of only lower case english character and numbers.

Example 

Input
logFileSize = 5
logLines =
[a1 9 2 3 1]
[g1 act car] [zo4 4 7]
[ab1 off key dog]
[a8 act zoo]

Output
[g1 act car]
[a8 act zoo]
[ab1 off key dog]
[zo4 4 7]
[a1 9 2 3 1]
'''

import re

def getLines(strng):
    lines = []
    for line in strng.split("\n") :
        lines.append(line)
        
    return lines

def getWords(line):
    line = line.replace("[", "")
    line = line.replace("]", "")
    words = line.split(" ")
    
    #print (words)
    return words

def isWordInt(word):
    if re.match(r'[0-9]+', word) : 
        return True
    else :
        return False
    
def constrDictsArrs(lines):
    strDict = {}
    intArr = []
    
    for line in lines :
        words = getWords(line)
        if isWordInt(words[1]) == True : intArr.append(line)
        else :
            strDict[words[0]] = " ".join(words[1:])
            
    #print(strDict)                   
    return strDict, intArr 


def sortStrLine(strDict):
    sortedArr = []
    idntfArr = list(strDict.keys())
    strArr = list(strDict.values())
    
    idntfArr.sort()
    strArr.sort()
    
    for st in strArr :
        for idnt in idntfArr :
            if strDict[idnt] == st :
                fullStr = "["+idnt+" "+st+"]"
                sortedArr.append(fullStr)
                idntfArr.remove(idnt)
                break      
    return sortedArr


def constrSortedLog(sortedStrArr, intArr):
    strng = "\n".join(sortedStrArr)
    intr = "\n".join(intArr)
    
    resOP = strng+"\n"+intr
    
    return resOP


def sortLogFile(logFileSize, logLines):
    lines = getLines(logLines)
    strDict, intArr = constrDictsArrs(lines)
    
    sortedArr = sortStrLine(strDict)
    
    resOP = constrSortedLog(sortedArr, intArr)
    
    print (resOP)
    
    
    
logFileSize = 5
logLines = '''[a1 9 2 3 1]
[g1 act car]
[zo4 4 7]
[ab1 off key dog]
[a8 act zoo]
[z1 act car]'''


sortLogFile(logFileSize, logLines)  
    
    
    
    

    
    
        
    
    
    




