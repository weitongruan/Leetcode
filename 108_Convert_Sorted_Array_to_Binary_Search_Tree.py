# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildhelper(nums)

    def buildhelper(self, slice):
        if not slice: return None
        i = (0 + len(slice)) / 2
        root = TreeNode(slice[i])
        root.left = self.buildhelper(slice[:i])
        root.right = self.buildhelper(slice[i + 1:])
        return root

    """ A little different
    """

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildhelper(nums, 0, len(nums) - 1)

    def buildhelper(self, nums, i, j):
        if i > j: return None
        index = (i + j) / 2
        root = TreeNode(nums[index])
        root.left = self.buildhelper(nums, i, index - 1)
        root.right = self.buildhelper(nums, index + 1, j)
        return root