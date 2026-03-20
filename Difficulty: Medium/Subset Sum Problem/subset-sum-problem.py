class Solution:
    def isSubsetSum (self, arr, sum):
        
        def backtrack(start,Currentsum):
            
            if Currentsum==sum:
               return True
               
            if Currentsum>sum or start==len(arr):
                return False
                
            for i in range(start,len(arr)):
                if backtrack(i+1,Currentsum+arr[i]):
                    return True
                    
            return False
            
        return backtrack(0,0)
               
            
            
        
        
        