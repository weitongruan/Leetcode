class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for s in magazine:
            dic[s] = dic.get(s, 0) + 1

        for s in ransomNote:
            if dic.get(s, 0):
                dic[s] -= 1
            else:
                return False

        return True