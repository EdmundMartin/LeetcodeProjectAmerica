from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        copy = root
        while list1 and list2:
            if list1.val < list2.val:
                next = list1.next
                list1.next = None
                copy.next = list1
                copy = copy.next
                list1 = next
            else:
                next = list2.next
                list2.next = None
                copy.next = list2
                copy = copy.next
                list2 = next
        remaining = list2 if list1 is None else list1
        copy.next = remaining
        return root.next