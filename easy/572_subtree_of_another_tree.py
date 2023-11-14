from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def are_equal(node_one, node_two):
    if node_one and node_two is None:
        return False
    if node_two and node_one is None:
        return False
    if node_one is None and node_two is None:
        return True
    if node_one.val != node_two.val:
        return False
    left_tree = are_equal(node_one.left, node_two.left)
    right_tree = are_equal(node_one.right, node_two.right)
    return left_tree and right_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if current_node.val == subRoot.val:
                if are_equal(current_node, subRoot):
                    return True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return False