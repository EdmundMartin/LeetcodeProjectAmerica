from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traverse(left: Optional[TreeNode], right: Optional[TreeNode]):
    if left is None and right is None:
        return True
    if left is None and right is not None:
        return False
    if left is not None and right is None:
        return False

    if left.val != right.val:
        return False
    left_side = in_order_traverse(left.left, right.left)
    right_side = in_order_traverse(left.right, right.right)
    return left_side and right_side


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return in_order_traverse(p, q)