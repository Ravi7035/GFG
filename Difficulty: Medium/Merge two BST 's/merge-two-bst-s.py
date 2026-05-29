'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def merge(self, root1, root2):
        # code here
        stack1=[]
        def solve1(curr,stack1):
            if not curr:
                return 
            
            stack1.append(curr.data)
            solve1(curr.left,stack1)
            solve1(curr.right,stack1)
            
        solve1(root1,stack1)
            
        stack2=[]
        def solve2(curr,stack2):
            if not curr:
                return 
            stack2.append(curr.data)
            solve2(curr.left,stack2)
            solve2(curr.right,stack2)
            
        solve2(root2,stack2)
        
        
        stack1.extend(stack2)
        
        stack1.sort()
        
        return stack1
        
     
        
        
            
        
        
            
            
        
        