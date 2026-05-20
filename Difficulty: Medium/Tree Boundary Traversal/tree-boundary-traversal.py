class Solution:

    def boundaryTraversal(self, root):

        if not root:
            return []

        ans = []

        #helper function to return whether the current node is leaf node or not.
        def isLeaf(node):

            return not node.left and not node.right

        #if the root is not the leaf node then add the data to answer
        if not isLeaf(root):
            ans.append(root.data)

        #getting the left boundary nodes excluding leaf nodes
        curr = root.left

        while curr:

            if not isLeaf(curr):
                ans.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        #getting leaf nodes 
        def addLeaves(node):

            if not node:
                return

            if isLeaf(node):
                ans.append(node.data)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        addLeaves(root)

        #gettinf the right boundary nodes excluding leaf nodes
        temp = []

        curr = root.right

        while curr:

            if not isLeaf(curr):
                temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        ans.extend(temp[::-1])

        return ans