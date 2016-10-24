class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """ DFS
        """

        if not grid:
            return 0

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '*'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

        """ BFS
        """


        if not grid:
            return 0

        count = 0
        stack = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    stack.append((i, j))
                    while stack:
                        ii, jj = stack.pop()
                        # for ii, jj in stack:
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == "1":
                            grid[ii][jj] = "*"
                            stack.extend([(ii - 1, jj), (ii + 1, jj), (ii, jj - 1), (ii, jj + 1)])
        return count