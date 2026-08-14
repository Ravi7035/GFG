class Solution:
    def isPossible(self, arr, s, x):
        values = [s]
        total = s
    
        for num in arr:
            new_value = total + num
            values.append(new_value)
            total += new_value
    
        for value in reversed(values):
            if value <= x:
                x -= value
    
            if x == 0:
                return True
    
        return False
            
            
        
        
        