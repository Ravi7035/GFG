class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        
        n = len(mat)
        m = len(mat[0])

        # Build 2D prefix sum
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def get_sum(top, left, bottom, right):
            return (
                prefix[bottom + 1][right + 1]
                - prefix[top][right + 1]
                - prefix[bottom + 1][left]
                + prefix[top][left]
            )

        result = []

        for i, j in queries:

            radius = 0
            answer = -1

            while True:

                top = i - radius
                bottom = i + radius
                left = j - radius
                right = j + radius

                # Outside matrix
                if top < 0 or bottom >= n or left < 0 or right >= m:
                    break

                ones = get_sum(top, left, bottom, right)

                if ones <= k:
                    answer = 2 * radius + 1
                    radius += 1
                else:
                    break

            result.append(answer)

        return result
            