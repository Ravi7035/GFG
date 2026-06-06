class Solution:
    def numOfWays(self, n: int, m: int) -> int:

        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]

        attacking = 0

        for r in range(n):
            for c in range(m):

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < m:
                        attacking += 1

        total = n * m * (n * m - 1)

        return total - attacking