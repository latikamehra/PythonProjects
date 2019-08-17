'''
Created on Aug 12, 2019

@author: latikamehra
'''

import pandas as pd
from math import sqrt
import pprint


age = [5,6,12,13,18,21,36,50,51,52]
salary = [0,0,5,5,100,500,1000,1500,1600,1700]

def computeCorr(setDict1, setDict2):
    terms = len(setDict1['original set'])
    multSum = 0
    for i in range(terms):
        multSum += (setDict1['original set'][i] - setDict1['mean']) * (setDict2['original set'][i] - setDict2['mean'])
        
    covariance = multSum/(terms)
    
    correlationCoeff = covariance/(setDict1['standard deviation']*setDict2['standard deviation'])
    
    return covariance, correlationCoeff
        

def getSetDets(xSet):
    resDict = {}
    resDict['original set'] = xSet
    total = 0
    terms = len(xSet)
    
    for x in xSet :
        total += x
    
    resDict['mean'] = total/terms
    
    sqSum = 0
    xmax = max(xSet)
    xmin = min(xSet)

    for x in xSet :
        sqSum += (x-resDict['mean'])**2
        
    resDict['variance'] = sqSum/terms
    
    resDict['standard deviation'] = sqrt(resDict['variance'])
    
    normXSet = xSet.copy()
    standXSet = xSet.copy()
    
    for i in range(terms) :
        normXSet[i] = (xSet[i] - xmin)/ (xmax - xmin)
        
        standXSet[i] = (xSet[i] - resDict['mean']) / resDict['standard deviation']
        
    
    resDict['normalized set'] = normXSet
    resDict['standardized set'] = standXSet
    
    return resDict
    
    
ageDict = getSetDets(age)
salDict = getSetDets(salary)

print ("\n\nAge Set :")
pprint.pprint(ageDict)
print ("\n\nSalary Set :")
pprint.pprint (salDict)

covar, corrCoef = computeCorr(ageDict, salDict)
        
print ("Covariance = "+str(covar))
print ("Correlation Coefficient = "+str(corrCoef))

normAgeDict = getSetDets(ageDict['normalized set'])
standAgeDict = getSetDets(ageDict['standardized set'])
print ("\n\nNormalized Age Set :")
pprint.pprint(normAgeDict)
print ("\n\nStandardized Age Set :")
pprint.pprint(standAgeDict)

normSalDict = getSetDets(salDict['normalized set'])
standSalDict = getSetDets(salDict['standardized set'])
print ("\n\nNormalized Salary Set :")
pprint.pprint(normSalDict)
print ("\n\nStandardized Salary Set :")
pprint.pprint(standSalDict)

  



