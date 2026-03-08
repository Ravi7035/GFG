class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        
        sq = [x*x for x in arr]
        st = set(sq)
        
        for i in range(n):
            for j in range(i+1, n):
                if sq[i] + sq[j] in st:
                    return True
                    
        return False