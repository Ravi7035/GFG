class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix=0
        register={}
        ans=0
        
        for i in range(len(arr)):
            
            prefix+=arr[i]
            
            if prefix==k:
                ans=i+1
                
            if prefix -k in register:
                ans=max(ans,i-register[prefix-k])
                
            if prefix not in register:
                register[prefix]=i
                
        return ans
                
