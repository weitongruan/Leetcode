class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i in xrange(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = i
            else:
                if abs(table[nums[i]] - i) <= k:
                    return True
                else:
                    table[nums[i]] = i
        return False