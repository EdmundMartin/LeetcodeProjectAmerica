from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, depth: int) -> int:
    if node is None:
        return depth
    depth += 1
    left = recursive_solve(node.left, depth)
    right = recursive_solve(node.right, depth)
    return max(left, right)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return recursive_solve(root, 0)
