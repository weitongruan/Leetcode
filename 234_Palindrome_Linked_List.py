# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """ Algorithm 1
        """
        fast = slow = head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next
        return not reverse

        """ Algorithm 2
        """
        fast = head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, head = head, reverse, head.next

        tail = head.next if fast else head
        isPali = True
        while reverse:
            isPali = isPali and reverse.val == tail.val
            head, head.next, reverse = reverse, head, reverse.next
            tail = tail.next
        return isPali
