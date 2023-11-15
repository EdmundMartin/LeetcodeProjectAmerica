from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = head
        while head:
            if head.next and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return ret
