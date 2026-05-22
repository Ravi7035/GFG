"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def Paths(self, root):
        # code here
        ans=[]
        def solve(node,temp):
            if not node:
                return
              
            temp.append(node.data)
            
            if not node.left and not node.right:
                ans.append(temp[:])
            
            solve(node.left,temp)
            solve(node.right,temp)
            
            temp.pop()
            
        solve(root,[])
        
        return ans
            
            
    
        