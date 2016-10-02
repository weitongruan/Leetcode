class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """ Use recursion but really slow
        """
        if rowIndex == 0:
            return [1]

        return map(lambda x, y: x + y, self.getRow(rowIndex - 1) + [0], [0] + self.getRow(rowIndex - 1))

        """ use O(k) extra space with map and lambda
        """
        if rowIndex == 0:
            return [1]
        else:
            old = [1]
            for i in xrange(rowIndex):
                new = map(lambda x, y: x + y, old + [0], [0] + old)
                old = new
            return new