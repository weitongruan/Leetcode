# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummy = ListNode(0)
        current = dummy

        heap= [(node.val, node) for node in lists if node]

        heapq.heapify(heap)

        while heap:
            current.next = heap[0][1]
            current = current.next
            if current.next:
                heapq.heapreplace(heap, (current.next.val, current.next))
            else:
                heapq.heappop(heap)
        return dummy.next

    # can also use Queue module