from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = None
        while head:
            if head.val == val:
                if prev:
                    prev.next = head.next
                head = head.next
            else:
                if dummy.next is None:
                    dummy.next = head
                prev = head
                head = head.next
        return dummy.next