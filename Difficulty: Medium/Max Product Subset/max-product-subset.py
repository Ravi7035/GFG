class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7

        n = len(arr)

        if n == 1:
            return arr[0]

        product = 1
        neg_count = 0
        zero_count = 0

        # Negative with smallest absolute value
        max_negative = -float('inf')

        for num in arr:
            if num == 0:
                zero_count += 1
                continue

            if num < 0:
                neg_count += 1
                max_negative = max(max_negative, num)

            product *= num

        # All zeros
        if zero_count == n:
            return 0

        # One negative and rest zeros
        if neg_count == 1 and zero_count + neg_count == n:
            return 0

        # Remove negative closest to zero if negatives are odd
        if neg_count % 2 == 1:
            product //= max_negative

        return product % MOD