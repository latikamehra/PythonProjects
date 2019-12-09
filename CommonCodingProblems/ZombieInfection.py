'''
Created on Dec 5, 2019

@author: latikamehra

Given a 2D grid, each cell is either a zombie or a human. Zombies can turn adjacent (up/down/left/right) human beings into zombies every day. Find out how many days does it take to infect all humans?
Input:
matrix, a 2D integer array where a[i][j] = 1 represents a zombie on the cell and a[i][j] = 0 represents a human on the cell.

Output:
Return an integer represent how many days does it take to infect all humans.
Return -1 if no zombie exists.

Example :
Input:
[[0, 1, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 0]]

Output:
2

Explanation:
At the end of the day 1, the status of the grid:
[[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[0, 1, 0, 1, 1],
[1, 1, 1, 0, 1]]

At the end of the day 2, the status of the grid:
[[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]]'''

import copy

def findZombieNeighbours(arrArr, row, col):
    rows = len(arrArr)
    cols = len(arrArr[0])
    
    possNeighbourLocs = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]

    flag = False
    
    #print (row, col)
    
    for neighLoc in possNeighbourLocs :
        r = neighLoc[0]
        c = neighLoc[1]
        
        #print (r,c)
        
        if r >= 0 and r<rows and c>=0 and c<cols :
            #print(arrArr[r][c])
            if arrArr[r][c] == 1 : flag = True
    
    #print (flag)
    return flag
            



def zombify(arrArr):
    rows = len(arrArr)
    cols = len(arrArr[0])
    
    day = 0
    
    anyHumansLeft = True
    
    while (anyHumansLeft) :
        newArrArr = copy.deepcopy(arrArr)
        #print (arrArr[2][0]) 
        anyHumansLeft = False
        flag = False
        print ("Array on Day "+str(day))
        print (arrArr)
        day = day + 1
    
        for row in range(0,rows) :
            for col in range(0,cols) :
                elem = arrArr[row][col]
                
                if elem == 0 : # If human, look for neighbours
                    flag = True
                    anyHumansLeft = True
                    isZombieNeighbour = findZombieNeighbours(arrArr, row, col)
                    
                    if isZombieNeighbour : 
                        #print ("There is a zombie in the neighbourhood")
                        newArrArr[row][col] = 1
        
        #print (arrArr[2][0])            
        arrArr = copy.deepcopy(newArrArr)       
                    
    if flag == False : day = day - 1                
    print ("Number of days needed for full zombification = "+str(day))
    
    
    
arrArr = [[0, 1, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 0]]  

 
zombify(arrArr)
    
