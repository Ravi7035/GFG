class Solution:
    def minToggle(self, arr):
        total_zeroes = arr.count(0)

        left_ones = 0
        right_zeroes = total_zeroes

        ans = float('inf')

        for x in arr:

            if x == 0:
                right_zeroes -= 1

            ans = min(ans, left_ones + right_zeroes)

            if x == 1:
                left_ones += 1

        ans = min(ans, left_ones + right_zeroes)

        return ans


            