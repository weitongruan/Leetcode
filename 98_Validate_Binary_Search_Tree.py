# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """ recursive algo
        """
        return self.helper(root, None, None)

    def helper(self, root, minNode, maxNode):
        if not root:
            return True
        if (minNode and minNode.val >= root.val) or (maxNode and root.val >= maxNode.val):
            return False
        return self.helper(root.left, minNode, root) and self.helper(root.right, root, maxNode)


        """ inorder traversal
        """


        temp = self.inorder(root)

        return temp == sorted(temp) and len(set(temp)) == len(temp)

    def inorder(self, root):
        ret = []
        if not root:
            return ret
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


    """ another way of coding inorder
    """

    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)