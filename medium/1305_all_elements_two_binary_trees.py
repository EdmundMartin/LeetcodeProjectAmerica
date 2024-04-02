from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traverse(node, seen):
    if node is None:
        return
    in_order_traverse(node.left, seen)
    seen.append(node.val)
    in_order_traverse(node.right, seen)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        seen = []
        in_order_traverse(root1, seen)
        in_order_traverse(root2, seen)
        return sorted(seen)