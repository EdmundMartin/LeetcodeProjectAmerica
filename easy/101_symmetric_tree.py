from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recursive_solve(left, right):
    if left is None and right is None:
        return True
    if left is None and right:
        return False
    if right is None and left:
        return False

    if left.val != right.val:
        return False
    l = recursive_solve(left.right, right.left)
    r = recursive_solve(left.left, right.right)
    return l and r


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return recursive_solve(root.left, root.right)