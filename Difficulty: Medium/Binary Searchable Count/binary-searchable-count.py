class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        def dfs(l, r, low, high):
            nonlocal ans

            if l > r:
                return

            mid = (l + r) // 2

            if low < arr[mid] < high:
                ans += 1

            dfs(l, mid - 1, low, min(high, arr[mid]))
            dfs(mid + 1, r, max(low, arr[mid]), high)

        dfs(0, n - 1, float('-inf'), float('inf'))
        return ans