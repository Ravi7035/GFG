class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here
        
        n=len(h)
        
        dp=[[-1] * 2 for _ in range(n)]
        
        def solve(index,ishightask):
            
            if index >=n:
                return 0
                
            if dp[index][ishightask] != -1:
                
                return dp[index][ishightask]
                
            no_task=solve(index+1,False)
            
            low_effort_task= l[index]+solve(index+1,True)
            
            
            high_effort_task=0
            
            if not ishightask:
                
                high_effort_task=h[index]+solve(index+1,True)
                
                
            dp[index][ishightask]=max(no_task,low_effort_task,high_effort_task)
            
            return dp[index][ishightask]
            
            
        return solve(0,False)
        
        
        
        