# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self.dfs(node, {})

    def dfs(self, node, dic):
        if not node:
            return None
        if node not in dic:
            dic[node] = UndirectedGraphNode(node.label)
            dic[node].neighbors += [self.dfs(v, dic) for v in node.neighbors]
        return dic[node]