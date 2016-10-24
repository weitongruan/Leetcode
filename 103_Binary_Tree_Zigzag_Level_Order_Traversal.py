# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        cnt = 0
        if not root:
            return ret
        stack = [root]
        while stack:
            cnt += 1
            temp = []
            vals = []
            for x in stack:
                vals.append(x.val)
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)

            if cnt % 2 == 1:
                ret.append([v for v in vals])
            else:
                ret.append([v for v in reversed(vals)])

            stack = temp

        return ret

        """ Faster algo
        """

        res = []
        if not root:
            return res
        stackE = []
        stackO = []
        stackE.append(root)
        while stackE or stackO:
            sub = []
            if stackE:
                while stackE:
                    temp = stackE.pop()
                    if temp.left:
                        stackO.append(temp.left)
                    if temp.right:
                        stackO.append(temp.right)
                    sub.append(temp.val)
            else:
                while stackO:
                    temp = stackO.pop()
                    if temp.right:
                        stackE.append(temp.right)
                    if temp.left:
                        stackE.append(temp.left)
                    sub.append(temp.val)
            res.append(sub)
        return res