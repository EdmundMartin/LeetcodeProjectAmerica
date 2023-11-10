from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        current_node = head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            dummy.next = prev
            current_node = next_node
        return dummy.next