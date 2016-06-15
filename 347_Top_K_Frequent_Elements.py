from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """ First solution: rumtime: 116ms
        """
        counter = Counter(nums)
        rets = []
        for (integer, counts) in counter.most_common(k):
            rets.append(integer)
        return rets

        """ Use zip: runtime: 116ms
        """
        return zip(*collections.Counter(nums).most_common(k))[0]
        """ Use list comprehension: runtime: 132ms
        """
        return [i[0] for i in Counter(nums).most_common(k)]
        """ Use counter + heapq: runtime: 132ms
        """
        c = Counter(nums)
        return heapq.nlargest(k, c, key=lambda x: c[x])
        # return heapq.nlargest(k, c, c.get) # runtime: 148ms