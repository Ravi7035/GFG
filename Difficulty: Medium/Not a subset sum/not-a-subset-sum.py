class Solution:
    def findSmallest(self, arr):
        arr.sort()
        reachable=1
        
        for num in arr:
            if num > reachable:
                
                return reachable
                
            reachable+=num
            
            
        return reachable
            
        
      