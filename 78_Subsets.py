class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]
        for i in sorted(nums):
            res += [j + [i] for j in res]

        return res