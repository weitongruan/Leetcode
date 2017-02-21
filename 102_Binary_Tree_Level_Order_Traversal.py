# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        """ BFS
        """
        ret, level = [], [root]

        while root and level:
            ret.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ret

        """ My own BFS
        """

        result = []
        level = []

        if not root:
            return result

        level.append(root)

        while level:
            temp1 = []
            temp2 = []
            for node in level:
                temp2.append(node.val)
                if node.left:
                    temp1.append(node.left)
                if node.right:
                    temp1.append(node.right)
            level = temp1
            result.append(temp2)

        return result