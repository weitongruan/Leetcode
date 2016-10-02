class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """ First idea
        """
        return self.helper(s, t) & self.helper(t, s)

    def helper(self, s, t):
        table = {}
        for i in xrange(len(s)):
            if s[i] in table:
                if table[s[i]] != t[i]:
                    return False
            else:
                table[s[i]] = t[i]
        return True

        """ Second idea
        """

        table = {}
        for i in xrange(len(s)):
            if s[i] in table:
                if table[s[i]] != t[i]:
                    return False
            elif t[i] not in table.values():
                table[s[i]] = t[i]
            else:
                return False
        return True
