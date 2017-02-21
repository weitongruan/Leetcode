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

    ''' Recursive DFS
    '''
    def cloneGraph(self, node):

        def dfs(node, dic):
            if not node:
                return None

            if node not in dic:
                dic[node] = UndirectedGraphNode(node.label)
                for v in node.neighbors:
                    dic[node].neighbors.append(dfs(v, dic))

            return dic[node]

        return dfs(node, {})

    """ Iterative DFS
    """
    def cloneGraph(self, node):

        def dfs(node):

            if not node:
                return None
            dic = {}
            dic[node] = UndirectedGraphNode(node.label)
            stack = [node]
            while stack:
                v = stack.pop()
                for neighbor in v.neighbors:
                    if neighbor not in dic:
                        dic[neighbor] = UndirectedGraphNode(neighbor.label)
                        stack.append(neighbor)
                    dic[v].neighbors.append(dic[neighbor])

            return dic[node]

        return dfs(node)

    """ Iterative BFS
    """

    def cloneGraph(self, node):

        def bfs(node):

            if not node:
                return None
            dic = {}
            dic[node] = UndirectedGraphNode(node.label)
            queue = collections.deque([node])
            while queue:
                v = queue.popleft()
                for neighbor in v.neighbors:
                    if neighbor not in dic:
                        dic[neighbor] = UndirectedGraphNode(neighbor.label)
                        queue.append(neighbor)
                    dic[v].neighbors.append(dic[neighbor])

            return dic[node]

        return bfs(node)