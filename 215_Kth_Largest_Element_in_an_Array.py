from heapq import heapify, heappushpop


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapify(heap)

        for i in xrange(k, len(nums)):
            heappushpop(heap, nums[i])

        return heap[0]