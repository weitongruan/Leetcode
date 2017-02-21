# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """ Iterative
        """
        result, stack = [], []
        prev = None

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack[-1]
                if node.right and prev != node.right:
                    root = node.right
                else:
                    result += [node.val]
                    prev = stack.pop()
        return result

        """ Recursive
        """

        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]