from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        dq=deque()
        
        if start==end:
            return 0
            
        q=deque()
        q.append((start,0))
        
        visited=[False]*1000
        visited[start]=True
        
        while q:
            start,steps=q.popleft()
            
            for num in arr:
                new_num=(start*num)%1000
                if new_num==end:
                    return steps+1
                    
                if not visited[new_num]:
                    visited[new_num]=True
                    q.append((new_num,steps+1))
                    
                    
        return -1
                    
                