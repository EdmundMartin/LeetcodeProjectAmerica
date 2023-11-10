from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: TreeNode):
    if node.val == 0:
        return False
    if node.val == 1:
        return True

    left = recursive_solve(node.left)
    right = recursive_solve(node.right)
    if node.val == 2:
        return left or right
    return left and right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return recursive_solve(root)


if __name__ == '__main__':
    root_node = TreeNode(2)
    root_node.left = TreeNode(1)
    root_node.right = TreeNode(3)
    root_node.right.left = TreeNode(0)
    root_node.right.right = TreeNode(1)

