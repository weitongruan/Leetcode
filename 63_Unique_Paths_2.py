class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # if m == 1 and n == 1: return 1-obstacleGrid[m-1][n-1]
        Array = [[0] * n for _ in xrange(m)]

        i = 0
        while i < m:
            if obstacleGrid[i][0] != 1:
                Array[i][0] = 1
            else:
                break
            i += 1

        j = 0
        while j < n:
            if obstacleGrid[0][j] != 1:
                Array[0][j] = 1
            else:
                break
            j += 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    Array[i][j] = Array[i - 1][j] + Array[i][j - 1]

        return Array[m - 1][n - 1]