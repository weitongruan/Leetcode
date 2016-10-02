class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """ Hash Table
        """
        known_set = set()
        while n > 1 and (n not in known_set):
            known_set.add(n)
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
        return n == 1

        """ Recursion
        """
        if n == 1:
            return True
        elif n == 4:
            return False
        else:
            return self.isHappy(sum(map(lambda x: int(x) ** 2, list(str(n)))))