class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        """ First idea: runtime: 76ms
        """
        return reduce(lambda x, y: 26 * x + y, [ord(element) - 64 for element in list(s)])

        """ Another online runtime: 80ms
        """
        return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))