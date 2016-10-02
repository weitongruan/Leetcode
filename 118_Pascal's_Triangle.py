class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rets = []
        for idx in xrange(numRows):
            rets.append([])
            rets[idx].append(1)
            if idx >= 2:
                for jdx in range(1, idx):
                    rets[idx].append(rets[idx - 1][jdx - 1] + rets[idx - 1][jdx])
            if idx != 0:
                rets[idx].append(1)
        return rets

        """ with map and lambda
        """
        rets = [[1]]
        for idx in xrange(numRows):
           rets.append(map(lambda x, y: x+y, [0] + rets[-1], rets[-1] + [0]))
        return rets[:numRows]
        """ with zip
        """
