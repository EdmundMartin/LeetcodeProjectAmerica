from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(node: TreeNode):
    if node is None:
        return
    left, right = node.left, node.right
    node.left = right
    node.right = left
    invert_tree(left)
    invert_tree(right)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert_tree(root)
        return root