class Solution:
    def maxIndexDifference(self, s):
        # code here
        best = [-1] * 26
        ans = -1

        for i in range(len(s) - 1, -1, -1):
            c = ord(s[i]) - ord('a')

            if c == 25:          # 'z'
                reach = i
            elif best[c + 1] != -1:
                reach = best[c + 1]
            else:
                reach = i

            best[c] = max(best[c], reach)

            if c == 0:
                ans = max(ans, reach - i)

        return ans