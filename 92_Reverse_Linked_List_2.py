# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head

        fast, slow = dummy, dummy
        for _ in xrange(m - 1):
            fast = fast.next
            slow = slow.next
        tail = slow.next
        prev = ListNode(0)
        fast = fast.next
        for _ in xrange(n - m + 1):
            fast.next, prev, fast = prev, fast, fast.next
        slow.next, tail.next = prev, fast

        return dummy.next