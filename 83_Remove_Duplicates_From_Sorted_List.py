# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """ First idea
        """
        if head is not None:
            pter = head

            while pter.next is not None:
                if pter.next.val == pter.val:
                    pter.next = pter.next.next
                else:
                    pter = pter.next
        return head

        """ A shorter algo online
        """
        current = head

        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
