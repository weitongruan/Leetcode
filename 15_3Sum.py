class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in xrange(len(nums)):
            if nums[i] > 0:
                break
            target = -nums[i]
            tmp = {}
            for j in xrange(i + 1, len(nums)):
                x = target - nums[j]
                if x not in tmp:
                    tmp[nums[j]] = j
                else:
                    if [nums[i], nums[tmp[x]], nums[j]] not in res:
                        res.append([nums[i], nums[tmp[x]], nums[j]])
        return res


        """ Two pointers
        """

        res = []
        ret = []
        nums.sort()

        for i in xrange(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        res = set(res)
        for tuple in res:
            ret.append([tup for tup in tuple])

        return ret