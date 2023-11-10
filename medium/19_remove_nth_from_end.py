from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None

        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


def iterate_list(x):
    results = []
    while x:
        results.append(x.val)
        x = x.next
    print(results)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = Solution().removeNthFromEnd(head, 2)
    iterate_list(result)

    small = ListNode(1)
    small.next = ListNode(2)
    result = Solution().removeNthFromEnd(small, 1)
    iterate_list(result)