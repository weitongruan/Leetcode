# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        """ My solution:
        """
        if (p == None) & (q == None):
            return True
        elif (p != None) & (q != None):
            return bool((p.val == q.val) & self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right))
        else:
            return False

        """ A shorter version online:
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q
