from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traverse(node: TreeNode, result: List[int]):
    if node is None:
        return
    result.append(node.val)
    pre_order_traverse(node.left, result)
    pre_order_traverse(node.right, result)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        pre_order_traverse(root, result)
        return result
