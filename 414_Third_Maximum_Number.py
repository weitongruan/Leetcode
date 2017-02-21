class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """ Array (list) operation
        """

        ascendList = [-sys.maxint] * 3

        for i in nums:
            if i > ascendList[2]:
                ascendList[0], ascendList[1], ascendList[2] = ascendList[1], ascendList[2], i
            elif ascendList[2] > i > ascendList[1]:
                ascendList[0], ascendList[1] = ascendList[1], i
            elif ascendList[1] > i > ascendList[0]:
                ascendList[0] = i
        return ascendList[0] if ascendList[0] != - sys.maxint else ascendList[2]

        """ Use heap (or priority queue)
        """

        heap = [float('-inf')] * 3

        for i in nums:
            if i > heap[0] and i not in heap:
                heapq.heappushpop(heap, i)
        return heap[0] if heap[0] > float('-inf') else max(heap)
