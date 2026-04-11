class Solution:
    def countIncreasing(self, arr):
        # code here.
        #brute force..tryin out all possibilities using the two loops 
        output=0
        if len(arr)==1:
            return 0
            
        for i in range(len(arr)-1):
            
            for j in range(i+1,len(arr)):
                
                if arr[j] > arr[j-1]:
                    
                    output+=1
                    
                else:
                    
                    break
                    
        return output 
