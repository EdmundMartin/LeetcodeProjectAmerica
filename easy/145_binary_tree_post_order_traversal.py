from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def post_order_traverse(node: TreeNode, result: List[int]):
    if node is None:
        return
    post_order_traverse(node.left, result)
    post_order_traverse(node.right, result)
    result.append(node.val)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        post_order_traverse(root, result)
        return result
