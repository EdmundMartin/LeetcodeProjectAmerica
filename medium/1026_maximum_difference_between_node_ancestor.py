from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.current_max = float('-inf')

    def recursive_solve(self, node: TreeNode, min_ancestor, max_ancestor):
        if node is None:
            return

        max_ancestor_diff = max(abs(node.val - min_ancestor), abs(node.val - max_ancestor))
        if max_ancestor_diff > self.current_max:
            self.current_max = max_ancestor_diff
        new_min = min(node.val, min_ancestor)
        new_max = max(node.val, max_ancestor)
        self.recursive_solve(node.left, new_min, new_max)
        self.recursive_solve(node.right, new_min, new_max)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.recursive_solve(root, root.val, root.val)
        return self.current_max