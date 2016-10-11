# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        """ Iterative
        """
        low, high = 1, n

        while low < high:
            mid = (low + high) / 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

        """ Recursive
        """

        def firstBadVersion(self, n):
            """
            :type n: int
            :rtype: int
            """
            return self.binarysearch(1, n)

        def binarysearch(self, low, high):
            if low == high:
                return low
            mid = (low + high) / 2
            if isBadVersion(mid):
                return self.binarysearch(low, mid)
            else:
                return self.binarysearch(mid + 1, high)