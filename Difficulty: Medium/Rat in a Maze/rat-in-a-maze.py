class Solution:
    def ratInMaze(self, maze):
        result=[]
        if maze[0][0]==0 or maze[len(maze)-1][len(maze)-1]==0:
            return result
            
        directions=[
            (1,0,'D'),
            (-1,0,'U'),
            (0,-1,'L'),
            (0,1,'R')
            ]
            
        visited=[[False]*len(maze) for _ in range(len(maze))]
        
        def backtrack(row,col,path):
            if row==len(maze)-1 and col==len(maze)-1:
                result.append(path)
                return 
            
            visited[row][col]=True
            
            for curr_row,curr_col,move in directions:
                
                new_row=row+curr_row
                new_col=col+curr_col
                
                if 0 <=new_row < len(maze) and 0 <= new_col < len (maze) and maze[new_row][new_col]==1 and not visited[new_row][new_col]:
    
                    backtrack(new_row,new_col,path+move)
                    
            visited[row][col]=False
            
            
        backtrack(0,0,"")
        
        result.sort()
        return result
        
        