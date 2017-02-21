class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ One pointer
        """

        if not nums:
            return 0
        else:
            max_pre = min_pre = max_now = min_now = nums[0]
            max_sofar = nums[0]
            for i in xrange(1, len(nums)):
                max_now = max(max(max_pre * nums[i], min_pre * nums[i]), nums[i])
                min_now = min(min(max_pre * nums[i], min_pre * nums[i]), nums[i])
                max_sofar = max(max_sofar, max_now)
                max_pre = max_now
                min_pre = min_now
            return max_sofar
