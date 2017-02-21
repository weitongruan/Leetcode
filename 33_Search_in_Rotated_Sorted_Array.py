class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        L, R = 0, len(nums) - 1
        if nums[L] == target:
            return L
        elif nums[R] == target:
            return R
        elif target < nums[L] and target > nums[R]:
            return -1

        while L < R:
            M = (L + R) / 2
            if nums[M] == target: return M
            if nums[M] > nums[R]:
                if target >= nums[L] and target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if target > nums[M] and target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        if nums[L] == target:
            return L
        else:
            return -1