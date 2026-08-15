class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        
        if n == 0:
            return 0

        s = str(n)
        length = len(s)

        ans = 0

        # Numbers having fewer digits than n
        for l in range(1, length):

            if d == 0:
                ans += 9 ** l
            else:
                ans += 8 * (9 ** (l - 1))

        # Numbers having same number of digits as n
        for i in range(length):

            cur = int(s[i])
            start = 1 if i == 0 else 0

            # Try digits smaller than current digit
            for digit in range(start, cur):

                if digit == d:
                    continue

                remaining = length - i - 1
                ans += 9 ** remaining

            # Current digit is forbidden
            if cur == d:
                return ans

        # n itself doesn't contain d
        return ans + 1