from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solution(node: TreeNode, depth: int, results):
    if node is None:
        return
    if node.left is None and node.right is None:
        results[depth].append(node.val)
    recursive_solution(node.left, depth + 1, results)
    recursive_solution(node.right, depth + 1, results)


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        results = defaultdict(list)
        recursive_solution(root, 0, results)
        max_depth = max(results.keys())
        return sum(results[max_depth])