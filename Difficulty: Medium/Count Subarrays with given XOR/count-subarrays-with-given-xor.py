class Solution:
    def subarrayXor(self, arr, k):
        # code here
        xr=0
        frequency={0:1}
        count = 0
    
        for num in arr:
            xr ^= num
    
            count += frequency.get(xr ^ k, 0)
    
            frequency[xr] = frequency.get(xr, 0) + 1
    
        return count