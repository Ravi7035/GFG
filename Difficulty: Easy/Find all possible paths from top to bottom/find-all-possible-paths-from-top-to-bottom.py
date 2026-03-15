from typing import List
class Solution:
    def findAllPossiblePaths(self, n: int, m: int, mat: List[List[int]]) -> List[List[int]]:
        paths = []

        def backtrack(i, j, path):

            # out of bounds
            if i >= n or j >= m:
                return

            path.append(mat[i][j])

            # destination reached
            if i == n-1 and j == m-1:
                paths.append(path[:])
            else:
                backtrack(i, j+1, path)  # move right
                backtrack(i+1, j, path)  # move down

            path.pop()

        backtrack(0, 0, [])
        return paths[::-1]