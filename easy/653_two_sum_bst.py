from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, seen, target):
    if node is None:
        return False
    other = target - node.val
    if other in seen:
        return True
    seen.add(node.val)
    left_subtree = recursive_solve(node.left, seen, target)
    right_subtree = recursive_solve(node.right, seen, target)
    return left_subtree or right_subtree


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        return recursive_solve(root, seen, k)