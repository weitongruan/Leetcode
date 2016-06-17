class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ Not the first idea, but suddenly figure it out myself! Awesome! runtime: 52ms
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

        """ Good XOR algorithm online: definitely not constant extra space runtime: 84ms
        """
        return reduce(lambda x, y: x ^ y, nums + range(len(nums) + 1))

        """ XOR With constant extra space runtime: 72ms
        """
        ret = 0
        counter = 1
        for num in nums:
            ret ^= counter
            ret ^= num
            counter += 1
        return ret
