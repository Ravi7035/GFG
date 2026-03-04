class Solution:
    def maxSubarrayXOR(self, arr, k):
        #calculate the xored window of size k
        max_xor=0
        window=0
        for i in range(k):
            window^=arr[i]
        max_xor=window
        
        for i in range(k,len(arr)):
            window^=arr[i-k]
            window^=arr[i]
            max_xor=max(max_xor,window)
        return max_xor
        
        
        
        
       