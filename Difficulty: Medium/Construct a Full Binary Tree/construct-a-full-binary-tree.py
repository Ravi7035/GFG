''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        # code here
        n = len(pre)

        mp = {x: i for i, x in enumerate(preMirror)}
        preIdx = 0

        def build(l, h):
            nonlocal preIdx

            if preIdx >= n or l > h:
                return None

            root = Node(pre[preIdx])
            preIdx += 1

            if l == h or preIdx >= n:
                return root

            i = mp[pre[preIdx]]

            if i <= h:
                root.left = build(i, h)
                root.right = build(l + 1, i - 1)

            return root

        return build(0, n - 1)
        