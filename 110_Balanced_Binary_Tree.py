# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def depth(node):
            if not node:  # leaves
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if abs(left - right) > 1:
                raise Exception
            return max(left, right) + 1

        try:
            return abs(depth(root.left) - depth(root.right)) <= 1
        except:
            return False