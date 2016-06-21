# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """ Iteratively: runtime: 52ms
        """

        last = None
        currentNode = head
        while currentNode is not None:
            # nextNode = currentNode.next
            # currentNode.next = last
            # last = currentNode
            # currentNode = nextNode
            currentNode.next, last, currentNode = last, currentNode, currentNode.next
        return last

    """ Recursively: runtime 72ms
    """
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prevNode=None):
        # base case
        if not node:
            return prevNode
        nextNode = node.next
        node.next = prevNode
        return self._reverse(nextNode, node)



