class Solution:
    def knapSack(self, val, wt, capacity):
        n=len(val)
        dp=[[0]*(capacity+1) for _ in range(len(wt))]
        
        #initializing the dp state 
        
        for i in range(capacity+1):
            if wt[0] <=i:
                dp[0][i]=(i // wt[0])*val[0]
        
        for index in range(1,len(wt)):
            for capacity in  range(capacity+1):
            
                
                
                not_take=0+dp[index-1][capacity]
                
                take=0
                
                if capacity >= wt[index]:
                    
                    take=val[index]+dp[index][capacity-wt[index]]
                    
                dp[index][capacity]=max(take,not_take)
                
            
            
        return dp[n-1][capacity]
                
        
        
        
        
        
