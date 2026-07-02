class Solution:
    def divisibleByK(self, arr, k):
        
        dp = [False] * k

        for num in arr:
        
            new = dp[:]
        
            # Start a new subset containing only num
            new[num % k] = True
        
            # Extend every existing subset
            for rem in range(k):
                if dp[rem]:
                    new[(rem + num) % k] = True
        
            dp = new
        
            if dp[0]:
                return True
        
               