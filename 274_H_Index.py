class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """ O(nlogn)
        """
        if not citations:
            return 0
        else:
            citations = sorted(citations)
            counter = 0
            index = len(citations) - 1
            while index >= 0 and counter < citations[index]:
                index -= 1
                counter += 1
            return counter

        """ "O(n) time and O(n) space"
        """

        if not citations:
            return 0
        else:
            CountTable, n = {}, len(citations)
            for entry in citations:
                j = min(entry, n)
                CountTable[j] = CountTable.get(j, 0) + 1
            current, sum = n, CountTable.get(n, 0)
            while current > sum:
                current = current - 1
                sum += CountTable.get(current, 0)
            return current