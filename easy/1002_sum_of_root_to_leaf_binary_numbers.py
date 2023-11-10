from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, current_path: str, results):
    if node is None:
        return
    if node.left is None and node.right is None:
        results.append(current_path + str(node.val))
        return
    recursive_solve(node.left, current_path + str(node.val), results)
    recursive_solve(node.right, current_path + str(node.val), results)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        results = []
        recursive_solve(root, "", results)
        return sum([int(val, 2)  for val in results])