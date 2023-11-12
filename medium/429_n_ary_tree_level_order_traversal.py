from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def solve_recursive(self, node: 'Node', level: int):
        if node is None:
            return 
        if len(self.result) - 1 < level:
            self.result.append([])
        self.result[level].append(node.val)
        for child in node.children:
            self.solve_recursive(child, level + 1)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.result = [
        ]
        self.solve_recursive(root, 0)
        return self.result
