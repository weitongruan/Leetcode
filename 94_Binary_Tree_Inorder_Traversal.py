# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ''' Recursive algo
        '''
        ret = []
        if not root:
            return ret

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        """ Iterative algo
        """
        ret = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret += [root.val]
                root = root.right

        return ret

