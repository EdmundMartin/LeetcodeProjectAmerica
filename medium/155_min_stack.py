
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            min_val = val
        else:
            min_val = min(val, self.stack[-1][-1])
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        val, min_val = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, min_val = self.stack[-1]
        return min_val