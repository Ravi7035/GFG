from bisect import bisect_left

class Solution:
    def minInsAndDel(self, a, b):
        n, m = len(a), len(b)

        # element -> index in b
        pos = {}
        for i, x in enumerate(b):
            pos[x] = i

        # convert a into indices
        arr = []
        for x in a:
            if x in pos:
                arr.append(pos[x])

        # O(n log n) LIS
        lis = []

        for x in arr:
            idx = bisect_left(lis, x)

            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x

        L = len(lis)

        return (n - L) + (m - L)