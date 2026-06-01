class Solution:
    def getComponents(self, V, edges):
        # code here
        ans=[]
        adj=[[]for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited=[False]*V
        
        def solve(node,component):
            visited[node]=True
            component.append(node)
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    solve(neighbour,component)
                    
        for node in range(V):
            if not visited[node]:
                component=[]
                solve(node,component)
                ans.append(component)
                
        return ans
            
            
            
        
        