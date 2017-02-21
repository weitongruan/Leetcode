class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in xrange(1, 10):
            nums.append(i)
        res = []
        def dfs(target, n, begin, path):
            if target == 0 and n == 0:
                res.append(path)
                return
            if n > 0:
                for i in xrange(begin, len(nums)):
                    if nums[i] > target:
                        break
                    else:
                        dfs(target-nums[i], n-1, i+1, path+[nums[i]])
            return
        dfs(n, k, 0, [])
        return res
