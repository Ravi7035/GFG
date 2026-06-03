class Solution:
    def freqInRange(self, arr, queries):
        # code here
        from bisect import bisect_left,bisect_right
        from collections import defaultdict
        ans=[]
            
        positions=defaultdict(list)
        for i,num in enumerate(arr):
            positions[num].append(i)
            
            
        for l,r,x in queries:
            
            pos=positions[x]
            
            left=bisect_left(pos,l)
            right=bisect_right(pos,r)
            
            ans.append(right-left)
            
        return ans