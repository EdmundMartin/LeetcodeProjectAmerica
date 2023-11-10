from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def recurse(node: 'Node', result):
    if node is None:
        return
    for child in node.children:
        recurse(child, result)
    result.append(node.val)


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        results = []
        recurse(root, results)
        return results