from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traverse(node: TreeNode, tot: int, target: int):
    if node is None:
        return False
    current_sum = tot + node.val
    if current_sum == target and node.left is None and node.right is None:
        return True
    left_side = in_order_traverse(node.left, current_sum, target)
    right_side = in_order_traverse(node.right, current_sum, target)

    return left_side or right_side


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        in_order_traverse(root, 0, targetSum)


if __name__ == '__main__':

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)
    root.left.left.left = TreeNode(7)

    Solution().hasPathSum(root, 22)