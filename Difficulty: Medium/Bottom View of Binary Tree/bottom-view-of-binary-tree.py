'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
    
        q=deque()
        
        top_nodes={}
        
        q.append((root,0))
        
        
        while q:
            
            node,line=q.popleft()
            
            top_nodes[line]=node.data
                
            if node.left:
                
                q.append((node.left,line-1))
                
            if node.right:
            
                q.append((node.right,line+1))
        ans=[]
                
        for line in sorted(top_nodes):
            ans.append(top_nodes[line])
            
            
        return ans