# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """ Recursive: Time limit exceeded
        """

        if not root:
            return 0

        if root.left and root.right:
            return max(self.rob(root.left.left) + self.rob(root.left.right) + self.rob(root.right.left) + self.rob(
                root.right.right) + root.val, self.rob(root.left) + self.rob(root.right))
        elif not root.left and root.right:
            return max(self.rob(root.right.left) + self.rob(root.right.right) + root.val, self.rob(root.right))
        elif root.left and not root.right:
            return max(self.rob(root.left.left) + self.rob(root.left.right) + root.val, self.rob(root.left))
        else:
            return root.val

        """ Another way to rewrite the above is:
        """
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))

        """ Use a DP table to reduce computation
        """

        Table1 = {}

        def helper(root, Table):
            if not root: return 0
            if root in Table:
                return Table[root]
            val = 0
            if root.left:
                val += helper(root.left.left, Table) + helper(root.left.right, Table)
            if root.right:
                val += helper(root.right.left, Table) + helper(root.right.right, Table)
            val = max(val + root.val, helper(root.left, Table) + helper(root.right, Table))
            Table[root] = val
            return val

        return helper(root, Table1)

        """ A better solution
        """

        def helper(root):
            if not root:
                return 0, 0
            left = helper(root.left)
            right = helper(root.right)

            return left[1] + right[1] + root.val, max(left[0], left[1]) + max(right[0], right[1])

        val = helper(root)
        return max(val[0], val[1])

