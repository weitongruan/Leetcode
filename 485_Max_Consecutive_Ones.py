class Solution(object):

    """ My approach
    """
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        fast, slow, res = 0, 0, 0
        if not len(nums):
            return 0

        while fast < len(nums):
            if nums[fast] == 1 and nums[fast] * nums[slow] == 0:
                slow = fast
            elif nums[fast] == 0 and nums[slow] == 1:
                res = max(res, fast - slow)
                slow = fast

            fast += 1

        if nums[slow] == 1:
            res = max(res, len(nums) - slow)
        return res

    """ Another good approach:
    """

    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)
        return ans