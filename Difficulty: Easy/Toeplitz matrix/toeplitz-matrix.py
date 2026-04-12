class Solution:
    def isToeplitz(self, mat):
        m=len(mat)
        n=len(mat[0])
        
        for i in range(1,m):
            for j in range(1,n):
                
                if mat[i][j]!=mat[i-1][j-1]:
                    return False
                    
        return True
        
        
        
        
       
        
        
        