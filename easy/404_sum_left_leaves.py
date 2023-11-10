from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_left_leaves(node: TreeNode, parent: TreeNode, result: List[int]):
    if node is None:
        return
    if node.left is None and node.right is None and parent is not None:
        if node == parent.left:
            result.append(node.val)
    sum_left_leaves(node.left, node, result)
    sum_left_leaves(node.right, node, result)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = []
        sum_left_leaves(root, None, result)
        return sum(result)