def reverseSort(nums, i, j):
    pt = i
    while pt <= (i + j) / 2:
        nums[pt], nums[i + j - pt] = nums[i + j - pt], nums[pt]
        pt += 1
    return


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0 and len(nums) != 1:

            pt = len(nums) - 1

            while pt > 0:
                if nums[pt] > nums[pt - 1]:
                    break
                else:
                    pt -= 1

            if pt == 0:
                reverseSort(nums, 0, len(nums) - 1)
            else:
                target = nums[pt - 1]
                pt2 = len(nums) - 1
                while pt2 > pt:
                    if nums[pt2] > target:
                        break
                    else:
                        pt2 -= 1
                nums[pt - 1], nums[pt2] = nums[pt2], nums[pt - 1]

                reverseSort(nums, pt, len(nums) - 1)