#User function Template for python3

class Solution:
    def solve(self, bt):
        bt.sort()
        time=0
        waiting_time=0
        
        for i in range(len(bt)):
            waiting_time+=time
            time+=bt[i]
            
        return waiting_time//len(bt)
            
        
        
            
        
        
        
            
            
        
     