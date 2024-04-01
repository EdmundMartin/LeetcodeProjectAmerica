from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, results: List[int], k: int):
    if node is None:
        return
    if len(results) == k:
        return
    recursive_solve(node.left, results, k)
    results.append(node.val)
    recursive_solve(node.right, results, k)


# 42ms - Beats 97.21% of users with Python3
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        recursive_solve(root, results, k)
        return results[k-1]