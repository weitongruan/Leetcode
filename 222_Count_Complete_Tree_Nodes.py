# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """ Use binary search
        """


        def binarysearch(root, count):
            while root:
                count += 1
                root = root.left
            return count

        levelcount = binarysearch(root, 0)
        count = 0
        if levelcount:
            i = 1
            count = 2 ** (levelcount - 1)

            while i < levelcount:
                node = root.right
                if binarysearch(node, i) == levelcount:
                    root = root.right
                    count += 2 ** (levelcount - 1 - i)
                else:
                    root = root.left
                i += 1
        return count
