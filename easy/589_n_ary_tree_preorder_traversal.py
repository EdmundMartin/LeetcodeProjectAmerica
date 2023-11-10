from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def recursive(node: 'Node', results: List[int]):
    if node is None:
        return
    results.append(node.val)
    for child in node.children:
        recursive(child, results)


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        results = []
        recursive(root, results)
        return results
