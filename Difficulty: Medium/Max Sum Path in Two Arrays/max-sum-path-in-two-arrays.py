class Solution:
    def maxPathSum(self, a, b):
        
        i = j = 0

        sumA = 0
        sumB = 0
        ans = 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                sumA += a[i]
                i += 1

            elif a[i] > b[j]:
                sumB += b[j]
                j += 1

            else:
                ans += max(sumA, sumB) + a[i]

                sumA = 0
                sumB = 0

                i += 1
                j += 1

        while i < len(a):
            sumA += a[i]
            i += 1

        while j < len(b):
            sumB += b[j]
            j += 1

        ans += max(sumA, sumB)

        return ans