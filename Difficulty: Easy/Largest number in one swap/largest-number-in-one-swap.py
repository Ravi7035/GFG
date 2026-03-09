class Solution:
    def largestSwap(self, s):
        s=list(s)
        left=right=-1
        max_value_index=len(s)-1
        for i in range(len(s)-1,-1,-1):
            if s[i] > s[max_value_index]:
                max_value_index=i
            
            if s[i]<s[max_value_index]:
                left=i
                right=max_value_index
                
        if left!=-1:
            s[left],s[right]=s[right],s[left]
            
        return "".join(s)
        
        
        
        
        
        
        
        