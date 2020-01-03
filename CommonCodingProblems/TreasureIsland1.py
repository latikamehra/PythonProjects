'''
Created on Dec 29, 2019

@author: latikamehra

You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as ‘X’ in a block of the matrix. ‘X’ will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
Other areas ‘O’ are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.
e.g.
Input
[
[‘O’, ‘O’, ‘O’, ‘O’],
[‘D’, ‘O’, ‘D’, ‘O’],
[‘O’, ‘O’, ‘O’, ‘O’],
[‘X’, ‘D’, ‘D’, ‘O’],
]

Output from aonecode.com
Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''

def navigateGrid(grid, start, path=[]):
    maxRows = len(grid)
    maxCols = len(grid[0])
    
    startRow = start[0]
    startCol = start[1]
    
    newPath = path.copy()
    newPath.append(start)
    
    #print (newPath)
    
    if startRow >= maxRows or startCol >= maxCols or startRow < 0 or startCol < 0 or start in path :
        return None
    elif grid[startRow][startCol] == 'D' :
        return None
    else :
    
        if grid[startRow][startCol] == 'X' :
            return [newPath]
        else :
            pathsToReturn = []
            goUp = (startRow-1, startCol)
            goDown = (startRow+1, startCol)
            goLeft = (startRow, startCol-1)
            goRight = (startRow, startCol+1)
            
            possPaths = [goUp, goDown, goLeft, goRight]
            
            for pp in possPaths :
                newPaths = navigateGrid(grid, pp, newPath)
                if newPaths != None :
                    for np in newPaths :
                        if np != None :
                            pathsToReturn.append(np)
                            
                            
            return pathsToReturn
                            

def smallestPath(possPaths): 
    if len(possPaths) > 0 :
        minSize = len(possPaths[0])
        minPath = possPaths[0]
        for path in possPaths :
            if len(path) < minSize :
                minPath = path
                minSize = len(path)
                
        return (minPath)
    else :
        return None
                         
     

grid = [
['O', 'O', 'O', 'O'],
['D', 'O', 'D', 'O'],
['O', 'O', 'O', 'O'],
['X', 'D', 'D', 'O'],
] 
    
allPossPaths = navigateGrid(grid, (0,0))
smallstPath = smallestPath(allPossPaths)

if smallstPath != None :
    print ("Shortest Path = ")
    print (smallstPath)
    print ("Number if steps required = ")
    print (len(smallstPath)-1)
else :
    print ("No viable paths found")