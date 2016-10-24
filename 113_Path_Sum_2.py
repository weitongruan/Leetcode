# Definition for a binary tree node.# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        return [[root.val]+ list for list in self.pathSum(root.left, sum - root.val)] + [[root.val] + list for list in \
                                        self.pathSum(root.right, sum - root.val)]