class Solution:
    def countSubstring(self, s):
        n = len(s)

        # Prefix sums
        pref = [0]
        cur = 0
        for ch in s:
            if ch == '1':
                cur += 1
            else:
                cur -= 1
            pref.append(cur)

        # Coordinate compression
        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            ans = 0
            while i > 0:
                ans += bit[i]
                i -= i & -i
            return ans

        ans = 0

        for x in pref:
            idx = rank[x]

            # Count previous prefix sums strictly smaller
            ans += query(idx - 1)

            update(idx)

        return ans