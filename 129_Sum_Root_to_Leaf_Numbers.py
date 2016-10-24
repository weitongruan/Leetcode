# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """ Recursive
        """
        return self.helper(root, 0)

    def helper(self, root, sum):
        if not root:
            return 0
        sum = 10 * sum + root.val
        if not root.left and not root.right:
            return sum
        return self.helper(root.left, sum) + self.helper(root.right, sum)


    