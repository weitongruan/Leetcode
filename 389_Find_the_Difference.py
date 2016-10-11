class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s:
        :type t: str
        :rtype: str
        """
        return chr(reduce(lambda x, y: x ^ y, map(ord, s + t)))
