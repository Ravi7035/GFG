# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        q=deque()
        q.append((root,0))
        sums={}
        output=[]
        while q:
            node,line=q.popleft()
            
            if line not  in sums:
                sums[line]=node.data
                
            else:
                sums[line]+=node.data
                
            if node.left:
                q.append((node.left,line-1))
                
            if node.right:
                q.append((node.right,line+1))
                
        for line in sorted(sums):
            output.append(sums[line])
            
        return output
            
            
        
            
            
        
        
        