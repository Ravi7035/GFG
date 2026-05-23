class Solution:
    def toSumTree(self, root):

        def solve(node):

            if not node:
                return 0

            # Store original value
            old_val = node.data

            # Recursively get subtree sums
            left_sum = solve(node.left)
            right_sum = solve(node.right)

            # Update current node
            node.data = left_sum + right_sum

            # Return total sum including original node value
            return old_val + node.data

        solve(root)