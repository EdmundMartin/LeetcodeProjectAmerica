from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        current_node = root
        while current_node:
            if current_node.val <= val:
                if current_node.right is None:
                    current_node.right = TreeNode(val)
                    return root
                current_node = current_node.right
            if current_node.val > val:
                if current_node.left is None:
                    current_node.left = TreeNode(val)
                    return root
                current_node = current_node.left
        return root