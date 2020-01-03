'''
Created on Dec 10, 2019

@author: latikamehra

In Amazon’s sort center, a computer system decides what packages are to be loaded on what trucks. All rooms and spaces are abstracted into space units which is represented as an integer. For each type of truck, they have different space units. For each package, they will be occupying different space units. As a software development engineer in sort centers, you will need to write a method:

Given truck space units and a list of product space units, find out exactly TWO products that fit into the truck. You will also implement an internal rule that the truck has to reserve exactly 30 space units for safety purposes. Each package is assigned a unique ID, numbered from 0 to N-1.

Assumptions:
You will pick up exactly 2 packages.
You cannot pick up one package twice.
If you have multiple pairs, select the pair with the largest package.

Input:
The input to the function/method consists of two arguments :
truckSpace , an integer representing the truck space.
packagesSpace , a list of integers representing the space units occupying by packages.

Output:
Return a list of integers representing the IDs of two packages whose combined space will leave exactly 30 space units on the truck.

Example
Input :
truckSpace = 90
packagesSpace = [1, 10, 25, 35, 60]
Output :
[2, 3]
'''

def findPackages(truckSpace, packageArr):
    
    packageSpaceSum = truckSpace - 30
    
    if packageSpaceSum <= 0 : return None 
    
    maxPack = 0
    
    bestComb = None
    
    for i in range(0, len(packageArr)-1) :
        if packageArr[i] >= packageSpaceSum : break
        else :
            for j in range((i+1), len(packageArr)) :
                if packageArr[i] + packageArr[j] == packageSpaceSum :
                    locMax = max(packageArr[i], packageArr[j])
                    if locMax > maxPack :
                        bestComb = [i,j]
                        maxPack = locMax
                        
        
        
    if bestComb != None :
        print (bestComb)
    else :
        print ("No solution")
        
        
        
        
truckSpace = 90
packagesSpace = [1, 10, 25, 35, 60]


findPackages(truckSpace, packagesSpace)