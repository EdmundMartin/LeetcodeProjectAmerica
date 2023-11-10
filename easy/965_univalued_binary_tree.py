from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, root_val: int):
    if node is None:
        return True
    if node.val != root_val:
        return False
    return recursive_solve(node.left, root_val) and recursive_solve(node.right, root_val)


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return recursive_solve(root, root.val)