class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """ My solution: runtim 72ms
        """
        if str(x)[-1] == 0:
            return self.reverse(int(str(x)[:-1]))
        elif x >= 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < 0x7FFFFFFF else 0
        else:
            return -int(str(x)[1:][::-1]) if int(str(x)[1:][::-1]) < 0x7FFFFFFF else 0