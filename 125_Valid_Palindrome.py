class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """ Algorithm 1
        """
        alnum_str = ''.join([i for i in s if i.isalnum()])

        if alnum_str.lower() == alnum_str[::-1].lower() or alnum_str == []:
            return True
        else:
            return False

        """ Algorithm 2
        """
        pter1, pter2 = 0, -1
        while pter1 < len(s) + pter2:
            if not s[pter1].isalnum():
                pter1 += 1
            elif not s[pter2].isalnum():
                pter2 -= 1
            elif s[pter1].lower() != s[pter2].lower():
                return False
            else:
                pter1 += 1
                pter2 -= 1
        return True