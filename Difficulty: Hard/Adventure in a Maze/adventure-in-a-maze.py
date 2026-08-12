class Solution:
    def findWays(self, grid):

        n = len(grid)
        modulo = 10**9 + 7
        dp=[[-1]*(n+1) for _ in range(n+1)]

        def solve(i, j):

            if i >= n or j >= n:
                return (0, 0)

            if i == n - 1 and j == n - 1:
                return (1, grid[i][j])
            
            if dp[i][j]  != -1:
                return dp[i][j]
                
            totalWays = 0
            maxAdventure = 0

            if grid[i][j] == 1 or grid[i][j] == 3:
                ways, adventure = solve(i, j + 1)

                totalWays += ways
                maxAdventure = max(maxAdventure, adventure)

            if grid[i][j] == 2 or grid[i][j] == 3:
                ways, adventure = solve(i + 1, j)

                totalWays += ways
                maxAdventure = max(maxAdventure, adventure)

            if maxAdventure != 0:
                maxAdventure += grid[i][j]

            dp[i][j]=totalWays % modulo, maxAdventure
            
            return dp[i][j]

        return list(solve(0, 0))