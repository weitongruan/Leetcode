# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        ret = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        ret += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]

        return ret or [str(root.val)]