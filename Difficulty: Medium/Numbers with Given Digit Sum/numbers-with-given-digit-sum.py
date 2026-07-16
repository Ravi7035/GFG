class Solution:
    def countWays(self, n, sum):
        # code here
        target=sum
        dp = [[-1] * ( target + 1) for _ in range(n + 1)]
 
        def solve(position,remaining):
            
            if position == n:
                return 1 if remaining == 0 else 0
                
            if dp[position][remaining] != -1:
                return dp[position][remaining]
                
            ans=0
            
            start = 1 if position == 0 else 0
            
            for d in range(start,10):
                if d <= remaining:
                    ans+=solve(position+1,remaining-d)
                    
            dp[position][remaining]=ans
            
            return dp[position][remaining]
            
        return solve(0,target) if solve(0,target) else -1
                    