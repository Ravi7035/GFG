class Solution:
    def removeSpaces(self, s):
        
        output=""
        for i in range(len(s)):
            
            if s[i]==" ":
                
                continue
            
            output+=s[i]
            
        return output