class Solution:
    
    def cntOnes(self, grid):
        
        m = len(grid)
        n = len(grid[0])

        visited = set()

        # DFS to mark boundary-connected 1s
        def dfs(i, j):

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == 0:
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # Traverse first and last row
        for j in range(n):

            if grid[0][j] == 1:
                dfs(0, j)

            if grid[m - 1][j] == 1:
                dfs(m - 1, j)

        # Traverse first and last column
        for i in range(m):

            if grid[i][0] == 1:
                dfs(i, 0)

            if grid[i][n - 1] == 1:
                dfs(i, n - 1)

        # Count trapped 1s
        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1

        return count