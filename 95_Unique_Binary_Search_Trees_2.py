# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        else:
            return self.generate(1, n)

    def generate(self, i, j):
        ret = []
        if i > j:
            ret.append(None)
        else:
            for k in xrange(i, j + 1):
                left = self.generate(i, k - 1)
                right = self.generate(k + 1, j)
                for subtreeleft in left:
                    for subtreeright in right:
                        root = TreeNode(k)
                        root.left = subtreeleft
                        root.right = subtreeright
                        ret.append(root)
        return ret
