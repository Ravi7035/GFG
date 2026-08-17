class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        
        Jump={}
        
        ladders=[]
        m=len(lad)
        
        i=0

        while i < m:
            ladders.append((lad[i],lad[i+1]))
            i+=2
            
        snakes=[]
        s=len(sn)
        
        j=0
        
        while j < s:
            snakes.append((sn[j],sn[j+1]))
            j+=2
        
        for u,v in ladders:
            Jump[u]=v
            
        for u,v in snakes:
            Jump[u]=v
            
        
        visited=[False]*(n*n+1)
        
        q=deque([(1,0)])
        
        visited[1]=True
        
        while q:
            
            pos,throws=q.popleft()
            
            if pos == n*n:
                return throws
                

            
            for dice in range(1,7):
                
                nxt=pos+dice
                
                if nxt > n*n:
                    continue
                
                if nxt in Jump:
                    nxt=Jump[nxt]
                    
                
                    
                if not visited[nxt]:
                    visited[nxt]=True
                    q.append((nxt,throws+1))
        
        return -1
                
        
                
                
            
        
                
            
            
                
                
        