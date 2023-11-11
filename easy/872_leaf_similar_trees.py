from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def leaf_values(node: TreeNode, leaves):
    if node is None:
        return
    if node.left is None and node.right is None:
        leaves.append(node.val)
    leaf_values(node.left, leaves)
    leaf_values(node.right, leaves)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_vals, right_vals = [], []
        leaf_values(root1, left_vals)
        leaf_values(root2, right_vals)
        return left_vals == right_vals