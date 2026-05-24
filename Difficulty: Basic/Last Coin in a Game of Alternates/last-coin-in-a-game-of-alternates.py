class Solution:
    def coin(self, arr):
        # code here
        left=0
        right=len(arr)-1
        
        while left < right:
            
            if arr[left] > arr[right]:
                left+=1
                
            elif arr[left] < arr[right]:
                right-=1
                
            else:
                if arr[left+1] > arr[right-1]:
                    left+=1
                else:
                    right-=1
                    
        return arr[left] 