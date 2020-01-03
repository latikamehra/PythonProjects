'''
Created on Dec 10, 2019

@author: latikamehra
Amazon is partnering with the linguistics department at a local university to analyze important works of English literature and identify patterns in word usage across different eras. To ensure a cleaner output. the linguistics department has provided a list of commonly used words (e.g., “an”, “the”. etc.) to exclude from the analysis. In the context of this search, a word is an alphabetic sequence of characters having no whitespace or punctuation.

Write an algorithm to find the most frequently used word in the text excluding the commonly used words.

Input:
The input to the function/method consists of two arguments:
literatureText: a string representing the block of text,
wordsToExclude: a list of strings representing the commonly used words to be excluded while analyzing the word frequency.

Output:
Return a list of strings representing the most frequently used word in the text or in case of a tie, all of the most frequently used words in the text..

Note:
Words that have a different case are counted as the same word. The order of words does not matter in the output list. All words in the ‘wordsToExclude’ list are unique. Punctuation should be treated as white space.

Example
Input :
literature Text = “Jack and Jill went to the market to buy bread and cheese. Cheese is Jack’s and Jill’s favorite food.”
wordsToExclude = [“and”, “he”, “the”, “to”, “is”. “Jack”, “Jill”]
Output :
[“cheese”, “s”]
'''
import re 
import string

def getWords(strng):
    
    strng = strng.lower()
    puncts = string.punctuation
    splitChars = r"[\s"+puncts+"’]+"
    
    #print (splitChars)
    words = re.split(splitChars, strng)
    
    return words
    
def removeCommons(words, exclusionList):
    cleanedWords = words.copy()
    
    exclusionList = [el.lower() for el in exclusionList]
    
    for w in words :
        if w in exclusionList :
            cleanedWords.remove(w)
            
    return cleanedWords
            

def freqCounter(words):
    counterDict = {}
    maxCount = 0
    
    for w in words:
        counterDict.setdefault(w,0)
        counterDict[w] += 1
        
        if counterDict[w] > maxCount : maxCount = counterDict[w]
        
    return (counterDict, maxCount)
        
        
def getMaxFreqWords(text, exclusionList):
    words = getWords(text)
    
    cleanedWords = removeCommons(words, exclusionList)
    
    counterDict, maxCount = freqCounter(cleanedWords)
    
    mostFreqWords = []
    
    for word, freq in counterDict.items() :
        if freq == maxCount : 
            mostFreqWords.append(word)
    
     
    return mostFreqWords        

text = 'Jack and Jill went to the market to buy bread and cheese. Cheese is Jack’s and Jill’s favorite food.'
wordsToExclude = ['and', 'he', 'the', 'to', 'is', 'Jack', 'Jill']

print(getMaxFreqWords(text,wordsToExclude))