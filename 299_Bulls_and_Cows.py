class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        table = {}
        for i in xrange(len(secret)):
            if secret[i] != guess[i]:
                table[secret[i]] += 1
            else:
                bulls += 1

        """ Second idea:
        """
        bulls = 0
        cows = 0
        table1 = {}
        table2 = {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in table1:
                    table1[secret[i]] = set([i])
                else:
                    table1[secret[i]].add(i)
                if guess[i] not in table2:
                    table2[guess[i]] = set([i])
                else:
                    table2[guess[i]].add(i)
        for ele in table2:
            if ele in table1:
                cows += min(len(table2[ele]), len(table1[ele]))

        return str(bulls) + 'A' + str(cows) + 'B'