class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)

        # ----------------------------
        # Forward LCS DP
        # L[i][j] = LCS(s1[:i], s2[:j])
        # ----------------------------
        L = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    L[i][j] = 1 + L[i - 1][j - 1]
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # ----------------------------
        # Backward LCS DP
        # R[i][j] = LCS(s1[i:], s2[j:])
        # ----------------------------
        R = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    R[i][j] = 1 + R[i + 1][j + 1]
                else:
                    R[i][j] = max(R[i + 1][j], R[i][j + 1])

        original = L[n][m]
        ans = 0

        # Try every insertion position
        for i in range(n + 1):

            used = set()

            # Try matching inserted character with every position in s2
            for j in range(m):

                if L[i][j] + R[i][j + 1] == original:

                    ch = s2[j]

                    if ch not in used:
                        ans += 1
                        used.add(ch)

        return ans