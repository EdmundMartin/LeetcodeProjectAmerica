from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Result:
    def __init__(self, depth, parent):
        self.depth = depth
        self.parent = parent


class Solution:

    def __init__(self):
        self.x_node = None
        self.y_node = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        queue = [(root, None, 1)]
        while queue and (self.x_node is None or self.y_node is None):
            current_node, parent, depth = queue.pop(0)

            if current_node.val == x:
                self.x_node = Result(depth, parent)
            if current_node.val == y:
                self.y_node = Result(depth, parent)

            if current_node.left:
                queue.append((current_node.left, current_node, depth + 1))
            if current_node.right:
                queue.append((current_node.right, current_node, depth + 1))

        if self.x_node.parent == self.y_node.parent:
            return False
        if self.x_node.depth != self.y_node.depth:
            return False
        return True