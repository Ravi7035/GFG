class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code here
        m=len(mat)
        n=len(mat[0])
        
        if mat[xs][ys]==0 or mat[xd][yd]==0:
            return -1
            
        visited = [[False] * n for _ in range(m)]
        
        
        def dfs(i,j):
      
            if i==xd and j==yd:
                return 0
                
            visited[i][j]=True
            ans=float('-inf')
                
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dx,dy in directions:
                nx=i+dx
                ny=j+dy
                
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny]==1 and not visited[nx][ny]:
                    
                    ans=max(ans,1+dfs(nx,ny))
                    
            visited[i][j]=False
            
            return ans
            
        ans=dfs(xs,ys)
        
        return ans
                    
                    
        
            
            
        
            