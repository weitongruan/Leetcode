class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """ First idea: runtime: 60ms
        """
        counter = 0
        for p1 in xrange(len(nums)):
            if nums[p1] == val:
                counter += 1
            else:
                nums[p1-counter] = nums[p1]
        return len(nums) - counter

        """ Second idea: 56ms
        """
        counter = 0
        for p1 in xrange(len(nums)):
            if nums[p1] != val:
                nums[counter] = nums[p1]
                counter += 1

        return counter

        """ One algorithm online: 52ms
        """

        while val in nums:
            nums.remove(val)
        return len(nums)
