from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode, level: int, results: List[List[int]]):
    if node is None:
        return
    if level >= len(results):
        results.append([])
    results[level].append(node.val)
    recursive_solve(node.left, level + 1, results)
    recursive_solve(node.right, level + 1, results)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        recursive_solve(root, 0, results)
        return results