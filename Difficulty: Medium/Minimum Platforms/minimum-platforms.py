class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        platforms=0
        max_platforms=0
        arr.sort()
        dep.sort()
        i=j=0
        while i < len(arr) and j < len(dep):
            
            if arr[i] <= dep[j]:
                i+=1
                platforms+=1
                max_platforms=max(platforms,max_platforms)
                
            else:
                platforms-=1
                j+=1
                
        return max_platforms
            
        
        