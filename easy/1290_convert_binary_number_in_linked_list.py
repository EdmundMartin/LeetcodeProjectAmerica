

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = ""
        while head:
            result += str(head.val)
            head = head.next
        return int(result, 2)
