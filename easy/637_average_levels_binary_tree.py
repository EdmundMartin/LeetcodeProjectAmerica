from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, depth, results):
    if node is None:
        return
    results[depth].append(node.val)
    recursive_solve(node.left, depth + 1, results)
    recursive_solve(node.right, depth + 1, results)


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = defaultdict(list)
        recursive_solve(root, 0, results)
        max_depth = max(results.keys())
        return [
            sum(results.get(r)) / len(results.get(r)) for r in range(max_depth + 1)
        ]