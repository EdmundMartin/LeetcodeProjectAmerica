

class LinkedListNode:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.linked_list = LinkedListNode(homepage)

    def visit(self, url: str) -> None:
        node = LinkedListNode(url)
        node.prev = self.linked_list
        node.prev.next = node
        self.linked_list = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.linked_list.prev:
            self.linked_list = self.linked_list.prev
            steps -= 1
        return self.linked_list.value

    def forward(self, steps: int) -> str:
        while steps > 0 and self.linked_list.next:
            self.linked_list = self.linked_list.next
            steps -= 1
        return self.linked_list.value


if __name__ == '__main__':
    history = BrowserHistory("leetcode.com")
    history.visit()