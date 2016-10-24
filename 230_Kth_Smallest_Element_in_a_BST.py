# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """ Inorder Traversal
        """
        """ Recursive
        """
        list = self.inorderTraversal(root)
        return list[k - 1]

    def inorderTraversal(self, root):
        ret = []
        if not root:
            return ret
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        """ Iterative
        """


        stack = []
        count = 0
        # ret = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                # ret.append(root.val)
                count += 1
                if count == k:
                    return root.val
                root = root.right