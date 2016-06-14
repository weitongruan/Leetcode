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

        """ One solution: O(n) time but O(n) space : runtime 220ms
        """
        list1 = []
        list2 = []
        rets = []
        s = 1
        for idx in xrange(len(nums)):
            list1.append(s)
            s = s * nums[idx]
        s = 1
        for idx in xrange(len(nums) - 1, -1, -1):
            list2.append(s)
            s = s * nums[idx]
        for idx in xrange(len(list1)):
            rets.append(list1[idx] * list2[len(list2) - 1 - idx])
        return rets

        # I replace the index manipulation with list.reverse(), it's faster! runtime: 184ms

        list1 = []
        list2 = []
        rets = []
        s = 1
        for idx in xrange(len(nums)):
            list1.append(s)
            s = s * nums[idx]
        s = 1
        for idx in xrange(len(nums) - 1, -1, -1):
            list2.append(s)
            s = s * nums[idx]
        list2.reverse() # here is the reverse()
        for idx in xrange(len(list1)):
            rets.append(list1[idx] * list2[idx])
        return rets

        """ two lists are redundant, get rid of those can help achieve O(1) space. runtime: 168ms
        """
        rets = []
        s = 1
        for idx in xrange(len(nums)):
            rets.append(s)
            s = s * nums[idx]
        s = 1
        for idx in xrange(len(nums) - 1, -1, -1):
            rets[idx] *= s
            s = s * nums[idx]
        return rets
