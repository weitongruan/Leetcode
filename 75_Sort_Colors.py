class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        """ First idea: Counting Sort
        """
        count = [0] * 3
        for i in xrange(len(nums)):
            count[nums[i]] += 1
        idx = 0
        for i in xrange(len(count)):
            while count[i] > 0:
                nums[idx] = i
                idx += 1
                count[i] -= 1


        """ Second Idea: Dutch partition problem
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1