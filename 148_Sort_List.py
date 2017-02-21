# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        dummy = tail = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next
        tail.next = l1 or l2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))
        # same as self.merge(self.sortList(head), self.sortList(slow))