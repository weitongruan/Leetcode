class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        """Kahn's algorithm
        """

        graph = [[] for _ in xrange(numCourses)]
        edge = [0 for _ in xrange(numCourses)]
        result = []

        for t, f in prerequisites:
            graph[f].append(t)
            edge[t] += 1

        queue = collections.deque()

        for i in xrange(numCourses):
            if edge[i] == 0:
                queue.append(i)
        k = 0

        while queue:
            e = queue.popleft()
            k += 1
            result.append(e)
            for v in graph[e]:
                edge[v] -= 1
                if edge[v] == 0:
                    queue.append(v)

        return result if k == numCourses else []

        """ DFS
        """
        graph = [[] for _ in xrange(numCourses)]
        edge = [0 for _ in xrange(numCourses)]
        result = []

        for t, f in prerequisites:
            graph[f].append(t)

        def dfs(i):
            if edge[i] == -1:
                return False
            elif edge[i] == 1:
                return True

            edge[i] = -1
            for v in graph[i]:
                if not dfs(v):
                    return False
            edge[i] = 1
            result.append(i)
            return True

        for i in xrange(numCourses):
            if not dfs(i):
                return []
        result.reverse()
        return result