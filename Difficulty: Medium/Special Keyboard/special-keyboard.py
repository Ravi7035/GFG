class Solution:

    def optimalKeys(self, n: int) -> int:
        
        
        dp=[0] * (n+1)
        
        for operations in range(1,n+1):
            
            dp[operations]=operations
            
            for i in range(1,operations-2):
                
                current=dp[i]
                
                pastes=operations-i-2
                
                total=current*(pastes+1)
                
                
                dp[operations]=max(dp[operations],total)
                
                
        return dp[n]
        
       

          