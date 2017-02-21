class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(target, index, path):
            if target == 0:
                res.append(path)
                return
            for i in xrange(index, len(candidates)):
                if candidates[i] > target:
                    break
                if i-1 >= index and candidates[i] == candidates[i-1]:
                    continue
                dfs(target-candidates[i], i+1, path+[candidates[i]])
        dfs(target, 0, [])
        return res