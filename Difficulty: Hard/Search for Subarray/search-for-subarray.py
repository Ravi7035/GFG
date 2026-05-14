class Solution:

    def search(self, a, b):

        # Build LPS array
        lps = [0] * len(b)

        length = 0
        i = 1

        while i < len(b):

            if b[i] == b[length]:

                length += 1
                lps[i] = length
                i += 1

            else:

                if length != 0:
                    length = lps[length - 1]

                else:
                    lps[i] = 0
                    i += 1


        # KMP Search
        ans = []

        i = 0   # pointer for a
        j = 0   # pointer for b

        while i < len(a):

            # Match
            if a[i] == b[j]:

                i += 1
                j += 1

            # Full pattern matched
            if j == len(b):

                ans.append(i - j)

                j = lps[j - 1]

            # Mismatch
            elif i < len(a) and a[i] != b[j]:

                if j != 0:
                    j = lps[j - 1]

                else:
                    i += 1

        return ans