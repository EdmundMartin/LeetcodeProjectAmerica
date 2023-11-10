from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_in_range(node: TreeNode, results: List[int], low: int, high: int):
    if node is None:
        return
    if node.val >= low and node.val <= high:
        results.append(node.val)
    if node.val < low:
        search_in_range(node.right, results, low, high)
    elif node.val > high:
        search_in_range(node.left, results, low, high)
    else:
        search_in_range(node.left, results, low, high)
        search_in_range(node.right, results, low, high)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        results = []
        search_in_range(root, results, low, high)
        return sum(results)
