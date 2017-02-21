def swappairs(self, head):
    dummy = p0 = ListNode(0)
    dummy.next = head

    while p0.next and p0.next.next:
        p1, p2 = p0.next, p0.next.next
        p0.next, p1.next, p2.next = p2, p2.next, p1
        p0 = p0.next.next

    return dummy.next


