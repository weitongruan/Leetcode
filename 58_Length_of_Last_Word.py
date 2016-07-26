class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ First Idea: start from the end
        """
        fast = slow = -1
        marker = 0
        while fast >= -len(s):
            if s[slow] == " ":
                slow -= 1
            else:
                while fast >= -len(s):
                    if s[fast] == " ":
                        return slow - fast
                    else:
                        fast -= 1
                return slow - fast
            fast -= 1
        return 0


        """ Second idea: more pythonic: runtime: 50ms
        """

        list = s.split(" ")
        i = -1
        while i >= -len(list):
            if list[i]:
                return len(list[i])
            else:
                i -= 1
        return 0

        """ Another pythonic solution online: runtime 44ms
        """
        return len(s.rstrip().split(' ')[-1])

