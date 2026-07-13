class Solution:
    def minOperations(self, b):

        from math import gcd    
        MOD = 10**9 + 7
        n = len(b)

        visited = [False] * n
        lcm = 1

        for i in range(n):
            if not visited[i]:
                length = 0
                cur = i

                while not visited[cur]:
                    visited[cur] = True
                    cur = b[cur] - 1   # Convert to 0-based index
                    length += 1

                # Update LCM
                lcm = (lcm * length) // gcd(lcm, length)

        return lcm % MOD