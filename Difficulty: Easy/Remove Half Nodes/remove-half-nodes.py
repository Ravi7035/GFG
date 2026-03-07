class Solution:
    def RemoveHalfNodes(self, node):
        if node is None:
            return None
        
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        # if leaf node
        if node.left is None and node.right is None:
            return node
        
        # if only right child
        if node.left is None:
            return node.right
        
        # if only left child
        if node.right is None:
            return node.left
            
        return node
        
                
            
               
            
            