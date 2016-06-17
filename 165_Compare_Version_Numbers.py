class Solution(object):

    """ First Idea: didn't consider multiple dots
    """
    def levelSeparate(self, string):
        for i in xrange(len(string)):
            if string[i] == ".":
                return int(string[:i]), int(string[i + 1:])
        return int(string), 0

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_first, v1_second = self.levelSeparate(version1)
        v2_first, v2_second = self.levelSeparate(version2)
        if v1_first > v2_first:
            return 1
        elif v1_first == v2_first and v1_second > v2_second:
            return 1
        elif v1_first == v2_first and v1_second == v2_second:
            return 0
        elif v1_first == v2_first and v1_second < v2_second:
            return -1
        else:
            return -1

    """ Second try: runtime 57ms
    """

    def getResult(self, num1, num2):
        if num1 == 1:
            return 1
        elif num1 == 0:
            return num2
        else:
            return -1

    @staticmethod
    def compare(list1, list2):
        if int(list1[0]) > int(list2[0]):
            return 1
        elif int(list1[0]) == int(list2[0]):
            if len(list1) == 1:
                return 0
            else:
                return Solution.compare(list1[1:], list2[1:])
        else:
            return -1

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        k = min(len(v1), len(v2))
        if len(v1) > len(v2):
            return self.getResult(Solution.compare(v1[:k], v2[:k]), Solution.compare(v1[k:], [0] * (len(v1) - k)))
        elif len(v1) == len(v2):
            return Solution.compare(v1, v2)
        else:
            return self.getResult(Solution.compare(v1[:k], v2[:k]), Solution.compare([0] * (len(v2) - k), v2[k:]))

    """ I should use max instead of min : runtime: 54 ms
    """

    @staticmethod
    def compare(list1, list2):
        if int(list1[0]) > int(list2[0]):
            return 1
        elif int(list1[0]) == int(list2[0]):
            if len(list1) == 1:
                return 0
            else:
                return Solution.compare(list1[1:], list2[1:])
        else:
            return -1

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        k = max(len(v1), len(v2))
        return Solution.compare(v1 + [0]*(k-len(v1)), v2 + [0]*(k-len(v2)))

    """ use a loop instead of a recursive algorithm for compare:
    """

    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1;
        return 0;

