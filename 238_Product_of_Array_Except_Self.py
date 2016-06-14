class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ My solution: An easy implementation in Python, Time limit exceeded!
        """
        rets = []
        for i in xrange(len(nums)):
            if not i:
                rets.append(reduce(lambda x, y: x * y, nums[1:]))
            elif i == len(nums) - 1:
                rets.append(reduce(lambda x, y: x * y, nums[0:len(nums)]))
            else:
                rets.append(reduce(lambda x, y: x * y, nums[:i]) * reduce(lambda x, y: x * y, nums[i+1:]))
        return rets

        """ My solution: Use a dynamic programming table, Time limit exceeded!
        """
        Table = {}
        rets = []
        for idx in xrange(len(nums)):
            Table[(idx, idx)] = nums[idx]
            if idx:
                for jdx in xrange(idx):
                    Table[(jdx,idx)] = Table[(jdx, idx - 1)] * Table[(idx, idx)]

        for idx in xrange(len(nums)):
            if not idx:
                rets.append(Table[(1, len(nums) - 1)])
            elif i == len(nums) - 1:
                rets.append(Table[(0, len(nums) - 2)])
            else:
                rets.append(Table[(0, idx - 1)] * Table[(idx + 1, len(nums) - 1)])
        return rets

        """ One solution online:
        """
        