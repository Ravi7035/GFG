#User function Template for python3
class Solution:
	def minDifference(self, arr):
	    Total_sum=0
        for i in range(len(arr)):
            Total_sum+=arr[i]
            
        dp=[[False]*(Total_sum+1) for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][0]=True
            
        if arr[0] <= Total_sum:
            dp[0][arr[0]]=True
            
        for index in range(1,len(arr)):
            for j in range(1,Total_sum+1):
                
                not_take=dp[index-1][j]
                
                take=False
                
                if j >= arr[index]:
                    take=dp[index-1][j-arr[index]]
                    
                dp[index][j]=not_take or take

        minimum=float('inf')
                
        for i in range(0,Total_sum//2+1):
            
            if dp[len(arr)-1][i]:

                minimum=min(minimum,abs((Total_sum-i)-i))

        return minimum
                
                
                
                
                
            
                
                
        
        

        
	