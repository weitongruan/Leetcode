class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        if k:
            start = 0
            pter = 0
            temp = nums[0]
            for i in xrange(len(nums)):
                if (pter + k) % len(nums) == start:
                    nums[start], temp, pter, start = temp, nums[start + 1], start + 1, start + 1
                else:
                    nums[(pter + k) % len(nums)], temp, pter = temp, nums[(pter + k) % len(nums)], (pter + k) % len(
                        nums)