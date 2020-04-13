class Solution:
    def numIslands(self, grid):
        count=0 #to count number of islands
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.dfs(grid, i, j)
                    count=count+1   #increment the number of islands
        
        return count
    
    def dfs(self, grid, i, j):
        #skip the dfs check if the current element is water or previosuly marked land
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:  
                                              return
        
        #mark this newly visited land element
        grid[i][j]='@'
        
        #check all the adjacent elements to find land
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)  
    
    
    
grid = [[1,1,0,0],
        [1,0,0,0],
        [1,0,0,1]]    

    
grid = [[1,1,0,0],
        [0,0,1,0],
        [0,0,0,0],
        [1,0,1,1],
        [1,1,1,1]]



sol = Solution()
print (sol.numIslands(grid))
    