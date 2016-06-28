class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ First idea, I realized that this gives the length of the largest subsequence instead of the substring
        """
        if len(s) > 1:
            case1 = self.lengthOfLongestSubstring(s[1:]) + 1 if s[0] not in set(s[1:]) \
                else self.lengthOfLongestSubstring(s[1:])
            case2 = self.lengthOfLongestSubstring(s[:-1]) + 1 if s[-1] not in set(s[:-1]) \
                else self.lengthOfLongestSubstring(s[:-1])
            return max(case1, case2)
        elif len(s) == 1:
            return 1
        else:
            return 0
        """ I can use brute force to try every possible subsequence, but it takes too much time, this might save some
        time but still exceeds the time limit
        """
        maxlength = 0
        for idx in xrange(len(s)):
            jdx = 0
            while idx + jdx < len(s) and s[idx + jdx] not in s[idx:idx + jdx]:
                jdx += 1
            if len(s[idx:idx + jdx]) > maxlength:
                maxlength = len(s[idx:idx + jdx])

        return maxlength

        """ A better implementation online: rumtime 112ms
        """
        maxlength, start = 0, 0
        used = {}
        for idx in xrange(len(s)):
            if s[idx] in used and used[s[idx]] >= start:
                start = used[s[idx]] + 1
            used[s[idx]] = idx
            maxlength = max(maxlength, idx-start+1)
        return maxlength

        """ A slight faster variants: runtime 104ms
        """
        maxlength, start = 0, 0
        used = {}
        for idx in xrange(len(s)):
            if s[idx] in used and used[s[idx]] >= start:
                start = used[s[idx]] + 1
            else:
                maxlength = max(maxlength, idx - start + 1)
            used[s[idx]] = idx
        return maxlength



