'''
Created on Dec 5, 2019

@author: latikamehra

Given a two 2D integer array, find the max score of a path from the upper left cell to bottom right cell. The score of a path is the minimum value in that path.
Moving only right & down
'''


def findPossPaths(grid, start, path=[]) :
    possPaths = []
    newPath = path.copy()
    newPath.append(start)
    
    maxRow = len(grid) - 1
    maxCol = len(grid[0]) - 1
    
    if start[0] == maxRow and start[1] == maxCol: # End point reached
        return [newPath]
    
    elif start[0] > maxRow or start[1] > maxCol :
        return None
    
    else :
        
        rightMove = (start[0], start[1]+1)
        downMove = (start[0]+1, start[1])
        
        possRightPaths = findPossPaths(grid, rightMove, newPath) 
        possDownPaths = findPossPaths(grid, downMove, newPath) 
        
        if possRightPaths!=None : possPaths += possRightPaths
        if possDownPaths!=None : possPaths += possDownPaths
        
        return possPaths
    

def scoreOfPath(grid,path):
    minScore = grid[path[0][0]][path[0][1]]
    scoreRow = path[0][0]
    scoreCol = path[0][1]
    
    for row, col in path[1:] :
        if grid[row][col] < minScore:
            minScore = grid[row][col]
            
            scoreRow = row
            scoreCol = col
            
            
    return (scoreRow,scoreCol)



def maxScore(grid,pathArr):
    bestPath = None
    maxScore = 0
    
    for path in pathArr :
        scoreRow, scoreCol = scoreOfPath(grid, path)
        
        scoreVal = grid[scoreRow][scoreCol]
        
        if scoreVal > maxScore :
            maxScore = scoreVal
            bestPath = path
            
            
            
    return (maxScore, bestPath)


def getMaxScoreAndPath(grid):
    possPath = findPossPaths(grid, (0,0))
    print (maxScore(grid, possPath))
    
            
        
                
    
grid = [[7,5,3],
        [2,0,9],
        [4,5,9]]

getMaxScoreAndPath(grid)
        
    
    
    