class Solution:
    def countCoordinates(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i, j, vis):
            vis[i][j] = True

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if (0 <= ni < n and
                    0 <= nj < m and
                    not vis[ni][nj] and
                    mat[ni][nj] >= mat[i][j]):

                    dfs(ni, nj, vis)

        # Station P (top + left)
        for i in range(n):
            dfs(i, 0, pacific)

        for j in range(m):
            dfs(0, j, pacific)

        # Station Q (bottom + right)
        for i in range(n):
            dfs(i, m - 1, atlantic)

        for j in range(m):
            dfs(n - 1, j, atlantic)

        ans = 0

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans += 1

        return ans