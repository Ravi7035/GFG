# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:

    def isSubTree(self, root1, root2):

        first_tree_traversal = []
        second_tree_traversal = []

        def inorder_traversal1(root):

            if not root:
                first_tree_traversal.append("N")
                return

            inorder_traversal1(root.left)
            first_tree_traversal.append(root.data)
            inorder_traversal1(root.right)

        def inorder_traversal2(root):

            if not root:
                second_tree_traversal.append("N")
                return

            inorder_traversal2(root.left)
            second_tree_traversal.append(root.data)
            inorder_traversal2(root.right)

        inorder_traversal1(root1)
        inorder_traversal2(root2)

        n = len(first_tree_traversal)
        m = len(second_tree_traversal)

        # check if second traversal exists inside first traversal
        for i in range(n - m + 1):

            match = True

            for j in range(m):

                if first_tree_traversal[i + j] != second_tree_traversal[j]:
                    match = False
                    break

            if match:
                return True

        return False