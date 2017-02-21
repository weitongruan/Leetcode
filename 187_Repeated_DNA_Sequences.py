class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            if substring in record:
                result.add(substring)
            else:
                record.add(substring)

        return list(result)