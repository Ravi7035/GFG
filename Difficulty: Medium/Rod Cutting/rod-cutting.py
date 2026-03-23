
class Solution:
    def cutRod(self, price):
        n=len(price)
        dp=[0]*(n+1)
        #initialzing the dp state 
        
            
        for index in range(n):
            rod_length=index+1
            for length in range(rod_length,n+1):
                
                dp[length]=max(dp[length],price[index]+dp[length-rod_length])

    
        return dp[n]
        
            
        
            
            
                
            
                
            

