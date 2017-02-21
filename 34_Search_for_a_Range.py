class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(target, mode):
            L, R = 0, len(nums) - 1
            while L <= R:
                M = (L + R) / 2
                if mode == 'left':
                    if target > nums[M]:
                        L = M + 1
                    else:
                        R = M - 1
                elif mode == 'right':
                    if target >= nums[M]:
                        L = M + 1
                    else:
                        R = M - 1
            return L if mode == 'left' else R

        left, right = binarySearch(target, 'left'), binarySearch(target, 'right')
        return [left, right] if left <= right else [-1, -1]