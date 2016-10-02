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
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            fast = head
            slow = ListNode('start')

            while fast and fast.next:
                if fast.val == fast.next.val:
                    while fast.next and fast.val == fast.next.val:
                        fast = fast.next
                    if slow.val == 'start':
                        head = fast.next
                    else:
                        slow.next = fast.next
                else:
                    slow = fast
                fast = fast.next
            return head
