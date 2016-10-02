class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_list = str.split(' ')
        if len(pattern) != len(word_list):
            return False
        else:
            table = {}

            for i in xrange(len(pattern)):
                if pattern[i] not in table:
                    if word_list[i] not in table.values():
                        table[pattern[i]] = word_list[i]
                    else:
                        return False
                else:
                    if table[pattern[i]] != word_list[i]:
                        return False
            return True