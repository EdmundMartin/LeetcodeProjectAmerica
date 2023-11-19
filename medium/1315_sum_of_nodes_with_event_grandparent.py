from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.sum = 0

    def recursive_solve(self, node: Optional[TreeNode], parent: Optional[TreeNode], grandad: Optional[TreeNode]):
        if node is None:
            return

        if grandad and grandad.val % 2 == 0:
            self.sum += node.val
        self.recursive_solve(node.left, node, parent)
        self.recursive_solve(node.right, node, parent)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.recursive_solve(root, None, None)
        return self.sum