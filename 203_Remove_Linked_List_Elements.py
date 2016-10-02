# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        """ Algorithm 1
        """
        if not head:
            return None

        pter = head
        while pter.next:
            if pter.next.val == val:
                pter.next = pter.next.next if pter.next.next else None
            else:
                pter = pter.next
        return head if head.val != val else head.next

        """ Algorithm 2
        """

        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy

        while (pointer.next):

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return dummy.next
