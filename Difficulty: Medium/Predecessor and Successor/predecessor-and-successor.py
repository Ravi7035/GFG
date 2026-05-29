'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        # code here
        pre=[None]
        suc=[None]
        def solve(root):
            
            if not root:
                return 
            
            if root.data < key:
                if pre[0] is None or root.data > pre[0].data:
                    pre[0]=root
                
            if root.data > key:
                if suc[0] is None or root.data < suc[0].data:
                    suc[0]=root
            solve(root.left)
            solve(root.right)
            
        solve(root)
        
        return [pre[0],suc[0]]
            
        
            
            
            
                
            
                
            
            
        