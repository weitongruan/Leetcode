# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):

    """ recursive
    """
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarysearch(1, n)

    def binarysearch(self, low, high):
        if low == high:
            return low
        mid = (low + high) / 2
        if not guess(mid):
            return mid
        elif guess(mid) == 1:
            return self.binarysearch(mid + 1, high)
        else:
            return self.binarysearch(low, mid - 1)

        """ iterative
        """

        low, high = 1, n
        while (low < high):
            mid = (low + high) / 2
            if not guess(mid):
                return mid
            elif guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low