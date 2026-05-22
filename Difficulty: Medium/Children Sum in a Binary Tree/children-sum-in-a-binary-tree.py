'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        def solve(root):
            
            if not root or (not root.left and not root.right):
                
                return True
                
            left=0
            right=0
            
            if root.left:
                left=root.left.data
                
            if root.right:
                right=root.right.data
                
            if left+right!=root.data:
                
                return False
                
                
            return solve(root.left) and solve(root.right)
            
            
        return solve(root)
            
            