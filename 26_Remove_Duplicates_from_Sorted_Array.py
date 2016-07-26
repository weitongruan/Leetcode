class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ First idea: time limit exceeded
        """
        if nums:
            p1 = 1
            counter = 0
            while p1 <= len(nums) - counter - 1:
                if nums[p1] == nums[p1 - 1]:
                    counter += 1
                    for p2 in xrange(p1, len(nums) - counter):
                        nums[p2], nums[p2 + 1] = nums[p2 + 1], nums[p2]
                else:
                    p1 += 1
            return len(nums) - counter

        else:
            return 0

        """ A good idea online: runtime: 98ms
        """

        if nums:
            p1 = 1
            counter = 0
            for p1 in xrange(1, len(nums)):
                if nums[p1] != nums[p1-1]:
                    counter += 1
                    num[counter] = nums[p1]

            return counter + 1
        else:
            return 0
