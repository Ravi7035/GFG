class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()
       
        
        def solve(x):
            count=0
            n=len(arr)
        
            for i in range(n-2):
                
                j=i+1
                k=n-1
                
                while j < k:
                    
                    if arr[i]+arr[j]+arr[k]<=x:
                        count+=k-j
                        j+=1
                        
                    else:
                        k-=1
                        
            return count
                        
        return solve(r) -solve(l-1)
            