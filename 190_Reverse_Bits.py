class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        """ Bit manipulation
        """
        ret = 0
        for i in xrange(32):
            ret += (n >> i & 1) << (31 - i)
        return ret

