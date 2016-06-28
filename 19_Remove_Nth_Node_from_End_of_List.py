# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """ First Idea: rumtime: 92ms
        """
        endNode = head
        tempNode = head
        counter = 1

        while endNode is not None:
            counter += 1
            if counter > n + 2:
                tempNode = tempNode.next
            endNode = endNode.next
        if counter == n + 1:
            return head.next
        elif counter == n + 2:
            head.next = head.next.next
            return head
        else:
            tempNode.next = tempNode.next.next
            return head

        """ An idea online: runtime: 56ms
        """
        fast, slow = head, head
        for _ in xrange(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return head
