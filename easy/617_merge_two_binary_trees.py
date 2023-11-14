from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recursive_solve(left: TreeNode, right: TreeNode):
    if left is None and right is None:
        return None
    if left and right is None:
        return left
    if right and left is None:
        return right
    node = TreeNode(left.val + right.val)
    node.left = recursive_solve(left.left, right.left)
    node.right = recursive_solve(left.right, right.right)
    return node


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return recursive_solve(root1, root2)