#User function Template for python3

class Solution:
    def wordBreak(self, dict, s):
        res=[]
        wordset=set(dict)
        
        def backtrack(start,path):
            if start==len(s):
                res.append(" ".join(path))
                return 
                
            for end in range(start+1,len(s)+1):
                
                word=s[start:end]
                
                if word in wordset:
                    path.append(word)
                    backtrack(end,path)
                    path.pop()
                    
        backtrack(0,[])
                    
        return res
                    
            
        
        