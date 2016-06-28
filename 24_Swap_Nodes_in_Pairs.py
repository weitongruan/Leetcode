# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """ First Idea: runtime: 56ms
        """

        if not head or not head.next:
            return head
        else:
            prev, prev.next = self, head
            while prev.next and prev.next.next:
                a = prev.next
                b = a.next
                prev.next, b.next, a.next = b, a, b.next
                prev = a
            return self.next

        """ an algorithm online: 56 ms
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

        """ an algorithm online : 48ms
        """
        dummyNode = p0 = ListNode(0)
        dummyNode.next = head

        while p0.next and p0.next.next:
            p1, p2 = p0.next, p0.next.next
            p0.next, p1.next, p2.next = p2, p2.next, p1
            p0 = p0.next.next

        return dummyNode.next



