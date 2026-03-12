'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        
        def dfs(node,CurrentSum):
            if not node:
                return False
                
            CurrentSum+=node.data
                
            if not node.left and not node.right:
                return CurrentSum==target
                
            return dfs(node.left,CurrentSum) or dfs(node.right,CurrentSum)
            
        return dfs(root,0)
        
       