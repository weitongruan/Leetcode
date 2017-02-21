class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        """ Kahn's algorithm
        """
        graph = [[] for _ in xrange(numCourses)]
        edge = [0 for _ in xrange(numCourses)]

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
            for v in graph[e]:
                edge[v] -= 1
                if edge[v] == 0:
                    queue.append(v)

        return k == numCourses


        """ DFS recursive
        """

        def canFinish(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: bool
            """
            graph = [[] for _ in xrange(numCourses)]
            edge = [0 for _ in xrange(numCourses)]

            for t, f in prerequisites:
                graph[f].append(t)

            def dfs(i):
                if edge[i] == -1:
                    return False  # -1 stands for marked temporarily (currently visiting)
                elif edge[i] == 1:
                    return True  # 1 means already visited
                elif edge[i] == 0:  # 0 means not seen previously
                    edge[i] = -1
                    for j in graph[i]:
                        if not dfs(j):
                            return False
                    edge[i] = 1
                    return True

            for i in xrange(numCourses):
                if not dfs(i):
                    return False
            return True