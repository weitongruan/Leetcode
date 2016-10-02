class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''Input: [7, 1, 5, 3, 6, 4]
           Output: 5
        '''
        """ First idea, brute force, slow
        """

        if len(prices) <= 1:
            return 0
        else:
            maxProfit = 0
            for i in xrange(1, len(prices)):
                temp_profit = max(map(lambda x: prices[i] - x, prices[:i]))
                if temp_profit > maxProfit:
                    maxProfit = temp_profit
            return maxProfit

        """ Second approach.
        """
        if len(prices) <= 1:
            return 0
        else:
            small, small_pot, large = prices[0], prices[0], prices[0]
            for i in xrange(1, len(prices)):
                if prices[i] > large:
                    large = prices[i]
                elif prices[i] < small:
                    if prices[i] < small_pot:
                        small_pot = prices[i]
                if prices[i] - small_pot > large - small:
                    small, large = small_pot, prices[i]
            return large - small