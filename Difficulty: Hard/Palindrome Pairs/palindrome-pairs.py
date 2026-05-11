class Solution:

    def palindromePair(self, arr):

        def ispalindrome(s):
            return s == s[::-1]

        mp = {}

        # store reversed lookup
        for i, word in enumerate(arr):
            mp[word] = i

        for i, word in enumerate(arr):

            for j in range(len(word) + 1):

                left = word[:j]
                right = word[j:]

                # Case 1:
                # left is palindrome
                # find reverse(right)
                if ispalindrome(left):

                    rev = right[::-1]

                    if rev in mp and mp[rev] != i:
                        return True

                # Case 2:
                # right is palindrome
                # find reverse(left)
                if j != len(word) and ispalindrome(right):

                    rev = left[::-1]

                    if rev in mp and mp[rev] != i:
                        return True

        return False