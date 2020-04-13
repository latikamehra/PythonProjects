def getNeighs(loc, grid):
    rows = len(grid)
    cols = len(grid[0])
    
    row = loc[0]
    col = loc[1]
    
    up = (row-1, col)
    down = (row+1, col)
    left = (row, col-1)
    right = (row, col+1)
    
    neighs = []
    
    #if row != 0 : neighs.append(up)
    if row != rows-1 : neighs.append(down)
    #if col != 0 :  neighs.append(left)
    if col != cols-1 : neighs.append(right)
    
    return neighs

def checkNeighs(loc, grid, alreadyCounted):  
    alreadyCountedSet = set(alreadyCounted) 
    alreadyCounted = list(alreadyCountedSet) # Remove duplicates
    
    neighs = getNeighs(loc, grid) 
    
    for neigh in neighs :
        if grid[neigh[0]][neigh[1]] == 1 :
            if neigh not in alreadyCounted :
                alreadyCounted.append(neigh)
            alreadyCounted = checkNeighs(neigh, grid, alreadyCounted)
    
    return alreadyCounted
    
    
def contParks(grid):
    rows = len(grid)
    cols = len(grid[0])
    cpCount = 0
    alreadyCounted = []
    
    for row in range(0, rows):
        for col in range(0,cols):
            loc = (row,col)
            
            if loc not in alreadyCounted :
                if grid[row][col] == 1 :
                    
                    flag = True
                    neighs = getNeighs(loc, grid)
                    for neigh in neighs :
                        if neigh in alreadyCounted:
                            flag = False
                    
                    alreadyCounted.append(loc)
                    alreadyCounted = checkNeighs(loc,grid,alreadyCounted)
                    
                    if flag == True :
                        print ("Counting for")
                        print (loc)
                        cpCount += 1
                
                    
                
    return cpCount        
    
    
    
grid = [[1,1,0,0],
        [1,0,0,0],
        [1,0,0,1]]    

    
grid = [[1,1,0,0],
        [0,0,1,0],
        [0,0,0,0],
        [1,0,1,1],
        [1,1,1,1]]




print (contParks(grid))
    