from heapq import *


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(small) > len(large):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        else:
            return (large[0] - small[0]) / 2.0



            # Your MedianFinder object will be instantiated and called as such:
            # obj = MedianFinder()
            # obj.addNum(num)
            # param_2 = obj.findMedian()