class Solution:
    def minCost(self, height):
        dp=[0]*len(height)
        def solve(i):
            if i == 0:
                return 0
            if dp[i]!=0:
                return dp[i]
    
            jump1 = solve(i-1) + abs(height[i] - height[i-1])
    
            jump2 = float('inf')
            if i > 1:
                jump2 = solve(i-2) + abs(height[i] - height[i-2])
    
            dp[i]=min(jump1, jump2)
            return dp[i]

        return solve(len(height)-1)
        
        
                
            