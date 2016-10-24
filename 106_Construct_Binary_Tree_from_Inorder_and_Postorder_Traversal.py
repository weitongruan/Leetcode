# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        di = {}
        dp = {}

        for i in xrange(len(inorder)):
            di[inorder[i]] = i
            dp[postorder[i]] = i

        return self.buildhelper(inorder, postorder, 0, len(inorder) - 1, 0, len(inorder) - 1, di, dp)

    def buildhelper(self, inorder, postorder, ii, ij, pi, pj, di, dp):
        if pi > pj or ii > ij: return None
        root = TreeNode(postorder[pj])
        i = di[postorder[pj]]
        root.left = self.buildhelper(inorder, postorder, ii, i - 1, pi, pi + i - ii - 1, di, dp)
        root.right = self.buildhelper(inorder, postorder, i + 1, ij, pi + i - ii, pj - 1, di, dp)
        return root