# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """ First Idea: runtime 72ms
        """

        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val <= l2.val:
            Node1, Node2 = l1, l2
            head = l1
        else:
            Node1, Node2 = l2, l1
            head = l2

        if not Node1.next:
            Node1.next = Node2
            return head
        else:
            while Node1.next:
                if Node1.next.val <= Node2.val:
                    Node1 = Node1.next
                elif Node2.next:
                    Node1.next, Node2.next, Node2 = Node2, Node1.next, Node2.next
                else:
                    Node1.next, Node2.next = Node2, Node1.next
                    return head
            if Node2:
                Node1.next = Node2

            return head

        """ Second Idea: A recursive algorithm: runtime: 60ms
        """

        if not l1:
            return l2
        elif not l2:
            return l1

        """
        if not l1 or not l2:
            return l1 or l2
        """

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


