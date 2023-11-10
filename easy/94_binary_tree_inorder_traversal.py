from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order(node: Optional[TreeNode], results: List[int]):
    if node is None:
        return
    in_order(node.left, results)
    results.append(node.val)
    in_order(node.right, results)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        in_order(root, result)
        return result