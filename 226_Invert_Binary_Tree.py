# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        """ My solution:
        """
        if root == None:
            return root
        else:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root

        """ Another one on line:
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
