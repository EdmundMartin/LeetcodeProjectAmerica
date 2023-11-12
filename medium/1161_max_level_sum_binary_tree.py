from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, level: int, levels):
    if node is None:
        return
    levels[level] += node.val
    recursive_solve(node.left, level + 1, levels)
    recursive_solve(node.right, level + 1, levels)


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)
        recursive_solve(root, 1, levels)
        max_value = 0
        max_level = 0
        for k, v in levels.items():
            if v > max_value:
                max_value = v
                max_level = k
        return max_level