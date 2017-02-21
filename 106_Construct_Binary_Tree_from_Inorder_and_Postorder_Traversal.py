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

    """ My recursive algo, slow because of linear-time search
    """

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:

            root = TreeNode(postorder[-1])

            l = len(inorder)

            for i in xrange(l):
                if inorder[i] == root.val:
                    root.left = self.buildTree(inorder[: i], postorder[: i])
                    root.right = self.buildTree(inorder[i + 1: l], postorder[i: l - 1])

            return root
        else:
            return None

    """ Use a dictionary for constant time search
    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == len(postorder) and len(inorder) != 0:

            idic = {}
            for i in xrange(len(inorder)):
                idic[inorder[i]] = i

            return self.helper(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1, idic)

        else:
            return None

    def helper(self, inorder, postorder, istart, iend, pstart, pend, idic):
        if istart > iend or pstart > pend:
            return None
        root = TreeNode(postorder[pend])
        i = idic[root.val]
        root.left = self.helper(inorder, postorder, istart, i - 1, pstart, pstart + i - 1 - istart, idic)
        root.right = self.helper(inorder, postorder, i + 1, iend, pstart + i - istart, pend - 1, idic)
        return root