'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        
        if not root:
            return 
        
        q=deque()
        
        top_nodes={}
        
        q.append((root,0))
        
        
        while q:
            
            node,line=q.popleft()
            
            if line not in top_nodes:
                
                top_nodes[line]=node.data
                
            if node.left:
                
                q.append((node.left,line-1))
                
            if node.right:
            
                q.append((node.right,line+1))
        ans=[]
                
        for line in sorted(top_nodes):
            ans.append(top_nodes[line])
            
            
        return ans
                
            
                
        
            
            
     
      