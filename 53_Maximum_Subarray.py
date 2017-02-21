class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ One pointer
        """

        if not nums:
            return 0
        else:
            sum, lsum = 0, nums[0]
            i = 0
            while i < len(nums):
                sum += nums[i]
                lsum = max(lsum, sum)
                sum = max(sum, 0)
                i += 1
            return lsum
