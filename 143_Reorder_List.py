class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, list):
        if len(list):
            self.head = ListNode(list[0])
        if len(list) > 1:
            currentNode = self.head
            for i in xrange(1, len(list)):
                nextNode = ListNode(list[i])
                currentNode.next = nextNode
                currentNode = nextNode
        else:
            currentNode = ListNode(list[0])
        currentNode.next = None

    def Print(self, head):
        list = []
        node = head
        while node is not None:
            list.append(node.val)
            node = node.next
        print list


    # @staticmethod
    # def reorderList(head):
    #     """
    #     :type head: ListNode
    #     :rtype: void Do not return anything, modify head in-place instead.
    #     """
    #
    #     """ First idea: A recursive algorithm but takes O(n^2) time: Time limit exceeded
    #     """
    #     prevNode = head
    #     if prevNode != None:
    #         lastNode = head.next
    #         if lastNode != None:
    #             noneNode = head.next.next
    #             if noneNode == None:
    #                 return None
    #         else:
    #             return None
    #     else:
    #         return None
    #
    #     while noneNode != None:
    #         prevNode, lastNode, noneNode = prevNode.next, lastNode.next, noneNode.next
    #
    #     head.next, lastNode.next, prevNode.next = lastNode, head.next, None
    #     Solution.reorderList(lastNode.next)
    #     return None

    """ Three steps: Divide into two halves, reverse the second half, merge!
    """

    def findHalfNode(self, head):
        half = head
        end = head
        while end.next is not None:
            half, end = half.next, end.next
            if end.next is not None:
                end = end.next
        middle = half.next
        half.next = None
        return head, middle

    def reverseList(self, head):

        last = None
        currentNode = head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode
        return last

        # if head is not None:
        #     currentNode = head.next
        #     preNode = head
        #     if currentNode is not None:
        #         nextNode = currentNode.next
        #         if nextNode is None:
        #             currentNode.next, preNode.next = preNode, None
        #             return currentNode
        #         else:
        #             while nextNode is not None:
        #                 currentNode.next = preNode
        #                 nextNode, currentNode = nextNode.next, nextNode
        #             currentNode.next = preNode
        #             head.next = None
        #             return currentNode
        #     return preNode

    def mergeList(self, head1, head2):
        # head1 is from first half, head2 is from second half. The former might be longer
        node1, node2 = head1, head2
        while node2 is not None:
            # node1.next, node1, node2.next, node2 = node2, node1.next, node1.next, node2.next
            a = node1.next
            b = node2.next
            # node1.next = node2
            # node2.next = a
            # node1 = a
            # node2 = b
            node1.next, node2.next, node1, node2 = node2, a, a, b

    def reorderList(self, head):
        if head is None:
            return None
        elif head.next is None:
            return None
        elif head.next.next is None:
            return None
        else:
            head1, head2 = self.findHalfNode(head)
            head2 = self.reverseList(head2)
            self.mergeList(head1, head2)
            return None


def main():
    s1 = Solution([1, 2, 3, 4, 5])
    s1.reorderList(s1.head)
    s1.Print(s1.head)

if __name__ == "__main__":
    main()