# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head:
            return head

        node = head
        len = 1
        while node.next:
            node = node.next
            len += 1
        kk = k % len
        if kk == 0:
            return head

        fast, slow = head, head
        for _ in xrange(kk):
            fast = fast.next
        if not fast:
            return slow
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next, fast.next, head = None, head, slow.next

        return head