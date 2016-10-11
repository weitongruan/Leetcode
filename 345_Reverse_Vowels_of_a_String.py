class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """ Algorithm 1
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        pter1, pter2 = 0, -1

        while pter1 < len(s) + pter2:
            if s[pter1] not in vowels:
                pter1 += 1
            elif s[pter2] not in vowels:
                pter2 -= 1
            else:
                s[pter1], s[pter2] = s[pter2], s[pter1]
                pter1 += 1
                pter2 -= 1
        return ''.join(s)

        """ Algorithm 2
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        pter1, pter2 = 0, -1

        while pter1 < len(s) + pter2:
            while pter1 < len(s) + pter2 and s[pter1] not in vowels:
                pter1 += 1
            while pter1 < len(s) + pter2 and s[pter2] not in vowels:
                pter2 -= 1

            s[pter1], s[pter2] = s[pter2], s[pter1]
            pter1 += 1
            pter2 -= 1
        return ''.join(s)