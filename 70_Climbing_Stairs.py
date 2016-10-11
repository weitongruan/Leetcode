class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        """ time limit exceeded
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


        """ DP
        """
        dic = {}
        dic[1] = 1
        dic[2] = 2

        for i in xrange(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]

        return dic[n]

        """ Fibonacci sequence
        """
        if n in {1, 2}:
            return n
        else:
            p = q = 1
            for _ in xrange(2, n + 1):
                p, q = q, p + q
            return q