#User function Template for python3

class Solution:
    def isPossible(self, a, b):
        #Code here
        if a != b and (a == 2 or b == 2):
            return True
        return False