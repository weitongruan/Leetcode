class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """ Two pointers
        """
        if not prices:
            return 0
        else:
            min, max, profit = prices[0], prices[0], 0
            for i in xrange(len(prices) - 1):
                if prices[i + 1] > prices[i]:
                    max = prices[i + 1]
                else:
                    profit += max - min
                    min, max = prices[i + 1], prices[i + 1]

            return profit + max - min