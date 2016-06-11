class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """ My solution: results in a time limit exceeded
        """
        list = []
        if len(s) == len(t):
            for letter in s:
                list.append(letter)
            for letter in t:
                if letter in list:
                    list.remove(letter)
                else:
                    return False
            return True
        """ Use dictionary
        """
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
        """ Use sort: faster
        """
        return sorted(s) == sorted(t)
        """ Use collections.Counter(): slower
        """
        return collections.Counter(t) == collections.Counter(s)
