from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def length_of_list(head: ListNode):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def move_forward_x(head: ListNode, x: int) -> ListNode :
    current_node = head
    for i in range(x):
        current_node = current_node.next
    return current_node


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size_of_a = length_of_list(headA)
        size_of_b = length_of_list(headB)
        diff = abs(size_of_a - size_of_b)

        if size_of_b > size_of_a:
            headB = move_forward_x(headB, diff)
        if size_of_a > size_of_b:
            headA = move_forward_x(headA, diff)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None