'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        prefix_sum={0:1}
        def dfs(node,curr_sum):
            if not node:
                return 0
                
            curr_sum+=node.data
            count=prefix_sum.get(curr_sum-k,0)
            prefix_sum[curr_sum]=prefix_sum.get(curr_sum,0)+1
            
            count+=dfs(node.left,curr_sum)
            count+=dfs(node.right,curr_sum)
            prefix_sum[curr_sum]-=1
            if prefix_sum[curr_sum]==0:
                del prefix_sum[curr_sum]
                
            return count
                
        return  dfs(root,0)
       