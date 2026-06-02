class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj=[[] for _ in range(V)]
		visited=[False]*V
		
		for u,v in edges:
		    
		        adj[u].append(v)
		        adj[v].append(u)
		        
		def dfs(node,parent):
		    visited[node]=True
		    
            for neighbour in adj[node]:
        	    if not visited[neighbour]:
                    if dfs(neighbour,node):
                        return True
                            
                elif parent != neighbour:
                    return True
                        
            return False
            
            
        for i in range(V):
            if not visited[i]:
                if dfs(i,-1):
                    return True
                    
        return False
                
            
            

    	            
    	   
    	            
    	  
		            
		          
		        
		