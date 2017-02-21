class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        combinations = [1] + [0]*target
        for i in xrange(target+1):
            for num in nums:
                if num  > i: break
                combinations[i] += combinations[i-num]
        return combinations[target]