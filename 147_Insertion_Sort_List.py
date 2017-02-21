# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current.next:
            if current.next.val < current.val:
                iterator = dummy
                while iterator.next.val < current.next.val:
                    iterator = iterator.next
                iterator.next, current.next.next, current.next = current.next, iterator.next, current.next.next
            else:
                current = current.next
        return dummy.next