from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        total = 0
        dummy = ListNode(0)
        prev = dummy
        head = head.next

        while head:
            if head.val == 0:
                node = ListNode(total)
                prev.next = node
                prev = node
                total = 0
            else:
                total += head.val
            head = head.next
        return dummy.next


if __name__ == '__main__':


    Solution().mergeNodes()