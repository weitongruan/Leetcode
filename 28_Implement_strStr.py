class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """ First Idea: runtime: 60ms
        """
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0
        else:
            for idx in xrange(0, len(haystack)-len(needle)+1):
                if haystack[idx:idx+len(needle)] == needle:
                    return idx

            return -1

        """ KMP algorithm:
        """
        if haystack == None or needle == None:
            return -1
        # generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            # needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
            print i, j, next[i], next[j]
        # check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1


