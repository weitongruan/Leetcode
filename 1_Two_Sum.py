class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ First idea: runtime 5604ms
        """
        for idx in xrange(len(nums) - 1):
            for jdx in xrange(idx, len(nums)):
                if nums[idx] + nums[jdx] == target:
                    return [idx, jdx]

        """ A good O(n) algorithm after reading some discussions online: runtime: 44ms
        """
        temp_dic = {}
        for idx in xrange(len(nums)):
            if nums[idx] not in temp_dic:
                temp_dic[target - nums[idx]] = idx
            else:
                return [temp_dic[nums[idx]], idx]
