class Solution(object):
    dp = [1, 1, 2, 5]
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(len(self.dp), n+1):
            self.dp.append(sum(self.dp[j] * self.dp[i-1-j] for j in xrange(i)))
        return self.dp[n]