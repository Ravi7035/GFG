class Solution:
    def knightTour(self, n):
        board=[[-1]*n for _ in range(n)]
        
        board[0][0]=0
        
        
        
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        
        def isSafe(x,y):
            return 0<=x<n and 0<=y<n and board[x][y]==-1
            
        def knightmove(x,y,step):
            
            if step==n*n:
                return True
            
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if isSafe(nx,ny):
                    
                    board[nx][ny]=step
                    
                    if knightmove(nx,ny,step+1):

                        return True
                        
                    board[nx][ny]=-1
                    
            return False
            
        if knightmove(0,0,1):
        
            return board 
        else:
            return []
                    
                
                    
            
                    
                    
                    
            
            
        
        
     
        
        