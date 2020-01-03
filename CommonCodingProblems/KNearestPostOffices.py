'''
Created on Dec 10, 2019

@author: latikamehra

Find the k post offices located closest to you, given your location and a list of locations of all post offices available.
Locations are given in 2D coordinates in [X, Y], where X and Y are integers.
Euclidean distance is applied to find the distance between you and a post office.
Assume your location is [m, n] and the location of a post office is [p, q], the Euclidean distance between the office and you is SquareRoot((m - p) * (m - p) + (n - q) * (n - q)).
K is a positive integer much smaller than the given number of post offices. 

e.g.
Input
you: [0, 0]
post_offices: [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

Output 
[[-1, 2], [0, 3], [4, 3]]
'''

def computeDist(yourPos, postOffice):
    xDiff = yourPos[0] - postOffice[0]
    yDiff = yourPos[1] - postOffice[1]
    
    distSqr = pow(xDiff,2) + pow(yDiff,2)
    dist = pow(distSqr,0.5)
    
    return dist


def kNearestPostOffices(yourPos, postOffices, k):
    distDict = {}
    
    for i in range(0, len(postOffices)) :
        dist = computeDist(yourPos, postOffices[i])
        
        distDict[i] = dist
        
    sortedList = []    
    for indx, dist in sorted(distDict.items(), key=lambda dist : dist[1]) :
        sortedList.append(postOffices[indx])
        
        
    return sortedList[0:k]



you = [0, 0]
post_offices = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

print (kNearestPostOffices(you, post_offices, k))