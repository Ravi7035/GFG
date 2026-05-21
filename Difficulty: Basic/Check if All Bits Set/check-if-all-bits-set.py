class Solution:
    def isBitSet(self, n):
        # code here
        binary_number=bin(n)[2:]
        
        answer=0
        
        for i in range(len(binary_number)):
            if int(binary_number[i]) != 1:
                return False
                
        return True
                