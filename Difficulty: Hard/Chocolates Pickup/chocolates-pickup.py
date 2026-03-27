class Solution:
    def maxChocolate(self, grid):
        
        m=len(grid)
        n=len(grid[0])
        dp=[[[-1]* (n) for _ in range(n)] for _ in range(m)]
        dx=[-1,0,1]
        dy=[-1,0,1]
        
        def solve(row,col1,col2):
            
            #base case
            
            
            
            if col1 < 0 or col1 >= n or col2 <0 or col2 >=n:
                return float('-inf')
                
            
            if dp[row][col1][col2] != -1:
                
                return dp[row][col1][col2]
            
            
            
            #if,at end of rows if the column of two robots are equal
            
            if row==m-1:
                
                if col1 ==col2:
                    
                    return grid[row][col1]
                    
                else:
                    return grid[row][col1] +grid[row][col2]
                    
                    
            #picking chocolates at that position
            
            chocolates=0
            
            if col1==col2:
                
                chocolates+=grid[row][col1]
                
            else:
                chocolates+=grid[row][col1]+grid[row][col2]
                
                
            max_chocolates=float('-inf')
            
            #choices  of the robots to move 
            
            for nx in dx:
                for ny in dy:
                    
                    max_chocolates=max(max_chocolates,chocolates+solve(row+1,col1+nx,col2+ny))
                    
            
            dp[row][col1][col2]= max_chocolates
            
            return dp[row][col1][col2]
            
            
        return solve(0,0,n-1)
                
                
                