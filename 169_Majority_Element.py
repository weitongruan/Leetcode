class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ First idea: runtime: 208ms
        """
        return heapq.nlargest(1, Counter(nums), key=lambda x: Counter(nums)[x])[0]

        """ Second idea: rumtime: 84ms
        """
        return Counter(nums).most_common(1)[0][0]
        """ A short one online:
        """
        return sorted(num)[len(num) / 2]