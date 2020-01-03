'''
Created on Dec 10, 2019

@author: latikamehra

You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point(marked as 'S') of the map and can move one block up, down, left or right at a time.
The treasure island is marked as ‘X’ in a block of the matrix.
Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
Other areas ‘O’ are safe to sail in.
Output the minimum number of steps to get to any of the treasure.
e.g.
Input
[
[‘S’, ‘O’, ‘O’, 'S', ‘S’],
[‘D’, ‘O’, ‘D’, ‘O’, ‘D’],
[‘O’, ‘O’, ‘O’, ‘O’, ‘X’],
[‘X’, ‘D’, ‘D’, ‘O’, ‘O’],
[‘X', ‘D’, ‘D’, ‘D’, ‘O’],
]

Output
3
Explanation
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''

def navigatePoint1To2(grid, start, end, path=[]):
    maxRows = len(grid)
    maxCols = len(grid[0])
    newPath = path + [start]
    pathSet = []
    
    if start in path :
        return None
    
    if start[0] < 0 or start[0] >= maxRows : # Check validity of starting point's Row number
        return None
    
    if start[1] < 0 or start[1] >= maxCols : # Check validity of starting point's Column number
        return None 
    
    startNodeVal = grid[start[0]][start[1]]
    
    if startNodeVal == 'D':
        return None
    
    if start == end :
        return [newPath]
    
    else :
        leftNode = [start[0], start[1]-1]
        rightNode = [start[0], start[1]+1]
        upNode = [start[0]-1, start[1]]
        downNode = [start[0]+1, start[1]]
        
        possNextNodes = [leftNode, rightNode, upNode, downNode]
        
        for node in possNextNodes :
            newPaths = navigatePoint1To2(grid, node, end, newPath)
            if newPaths != None :
                for np in newPaths :
                    if np != None :
                        pathSet.append(np)
                        
                
            
    '''print ("Start\t\tEnd\t\tExistingPath") 
    print (start, end, path)  
    print ("Returning path set")
    print (pathSet)'''
    return pathSet 


def getAllStartEnds(grid):
    allStarts = []
    allEnds = []
    
    for row in range(0, len(grid)) :
        for col in range(0, len(grid[0])) :
            
            if grid[row][col] == 'S' : allStarts.append([row,col])
            
            if grid[row][col] == 'X' : allEnds.append([row,col])
            
            
    return allStarts, allEnds


def getBestPath(grid):
    allStarts, allEnds = getAllStartEnds(grid)
    minSteps = None
    bestPath = None
    
    for start in allStarts :
        for end in allEnds :
            pathSets = navigatePoint1To2(grid, start, end, path=[])
            
            pathSets.sort(key=len)
            locBestPath = pathSets[0]
            locMinSteps = len(locBestPath) - 1
            
            if minSteps == None : 
                minSteps = locMinSteps
                bestPath = locBestPath
            else :
                if locMinSteps <  minSteps : 
                    minSteps = locMinSteps
                    bestPath = locBestPath
            
                
                
    print ("Best Path = ")
    print (bestPath)
    print ("Minimum Steps")
    print (minSteps)





grid = [
['S', 'O', 'O', 'S', 'S'],
['D', 'O', 'D', 'O', 'D'],
['O', 'O', 'O', 'O', 'X'],
['X', 'D', 'D', 'O', 'O'],
['X', 'D', 'D', 'D', 'O']
]

getBestPath(grid)


'''


grid = [
['O',  'S'],
['O', 'O'],
['O', 'O'],
['X', 'D']
]



pathSets = (navigatePoint1To2(grid, [0,1], [3,0]))

for ps in pathSets :
    print (ps)'''

