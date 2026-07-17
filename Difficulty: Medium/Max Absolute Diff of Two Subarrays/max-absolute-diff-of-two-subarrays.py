class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)

        leftMax = [0] * n
        leftMin = [0] * n
        rightMax = [0] * n
        rightMin = [0] * n

        # Left maximum subarray sums
        curr = leftMax[0] = arr[0]
        for i in range(1, n):
            curr = max(arr[i], curr + arr[i])
            leftMax[i] = max(leftMax[i - 1], curr)

        # Left minimum subarray sums
        curr = leftMin[0] = arr[0]
        for i in range(1, n):
            curr = min(arr[i], curr + arr[i])
            leftMin[i] = min(leftMin[i - 1], curr)

        # Right maximum subarray sums
        curr = rightMax[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            curr = max(arr[i], curr + arr[i])
            rightMax[i] = max(rightMax[i + 1], curr)

        # Right minimum subarray sums
        curr = rightMin[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            curr = min(arr[i], curr + arr[i])
            rightMin[i] = min(rightMin[i + 1], curr)

        ans = 0

        for i in range(n - 1):
            ans = max(
                ans,
                abs(leftMax[i] - rightMin[i + 1]),
                abs(leftMin[i] - rightMax[i + 1])
            )

        return ans
     
        