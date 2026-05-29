class Solution:
    def validGroups(self, s):

        n = len(s)

        memo = {}

        def solve(i, prev_sum):

            if i >= n:
                return 1

            if (i, prev_sum) in memo:
                return memo[(i, prev_sum)]

            total = 0
            curr_sum = 0

            for j in range(i, n):

                curr_sum += int(s[j])

                if curr_sum >= prev_sum:
                    total += solve(j + 1, curr_sum)

            memo[(i, prev_sum)] = total

            return total

        return solve(0, 0)