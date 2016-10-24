# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    def buildTree(self, preorder, inorder):
        dp = {}
        di = {}
        for i in range(len(preorder)):
            dp[preorder[i]] = i
            di[inorder[i]] = i
        return self.buildhelper(preorder, inorder, 0, len(preorder) - 1, 0, len(preorder) - 1, dp, di)

    def buildhelper(self, preorder, inorder, pi, pj, ii, ij, dp, di):
        if pi > pj: return None
        root = TreeNode(preorder[pi])
        i = di[root.val]
        root.left = self.buildhelper(preorder, inorder, pi + 1, pi + i - ii, ii, i - 1, dp, di)
        root.right = self.buildhelper(preorder, inorder, pi + i - ii + 1, pj, i + 1, ij, dp, di)
        return root


