# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.helper(root)
        return

    def helper(self, root):
        if not root:
            return None, None

        lroot, lrightmost = self.helper(root.left)
        rroot, rrightmost = self.helper(root.right)

        if not root.left and not root.right:
            return root, root
        elif not root.left and root.right:
            return root, rrightmost
        elif root.left and not root.right:
            root.left, root.right = None, lroot
            return root, lrightmost
        else:
            root.left, root.right, lrightmost.right = None, lroot, rroot
            return root, rrightmost

    """ Pre-order traversal
    """

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = [root]
        prev = None

        while stack:
            node = stack.pop()
            if prev:
                prev.left = None
                prev.right = node
            prev = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)