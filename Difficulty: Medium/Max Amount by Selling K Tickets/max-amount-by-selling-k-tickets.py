class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7
        # Python has min-heap, so store negatives
        heap = [-x for x in arr if x > 0]
        heapq.heapify(heap)

        profit = 0

        while k > 0 and heap:
            x = -heapq.heappop(heap)   # highest ticket price

            profit = (profit + x) % MOD

            x -= 1                     # one ticket sold

            if x > 0:
                heapq.heappush(heap, -x)

            k -= 1

        return profit
        
        