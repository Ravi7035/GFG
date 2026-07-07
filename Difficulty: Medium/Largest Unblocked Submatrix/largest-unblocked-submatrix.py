class Solution:
    def largestArea(self, n, m, arr):
 
        rows = [0]
        cols = [0]

        for r, c in arr:
            rows.append(r)
            cols.append(c)

        rows.append(n + 1)
        cols.append(m + 1)

        rows.sort()
        cols.sort()

        maxRowGap = 0
        for i in range(1, len(rows)):
            maxRowGap = max(maxRowGap, rows[i] - rows[i - 1] - 1)

        maxColGap = 0
        for i in range(1, len(cols)):
            maxColGap = max(maxColGap, cols[i] - cols[i - 1] - 1)

        return maxRowGap * maxColGap