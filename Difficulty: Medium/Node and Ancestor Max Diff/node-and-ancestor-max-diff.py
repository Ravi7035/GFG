''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        maximum=[float('-inf')]
        
        def solve(node,max_ancestor):
            
            if not node:
                return 
                
            maximum[0]=max(maximum[0],max_ancestor-node.data)
            
            max_ancestor=max(max_ancestor,node.data)
            
            solve(node.left,max_ancestor)
            solve(node.right,max_ancestor)
            
        if not root:
            return -1
            
        solve(root.left,root.data)
        solve(root.right,root.data)
            
            
        return maximum[0]