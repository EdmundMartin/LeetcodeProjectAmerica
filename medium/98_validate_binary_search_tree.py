from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 40ms - Beats 92.74% of users with Python3
def recursive_solve(node: TreeNode, min_val: int, max_val: int):
    if node is None:
        return True
    if node.val <= min_val:
        return False
    if node.val >= max_val:
        return False
    left_subtree = recursive_solve(node.left, min_val, node.val)
    right_subtree = recursive_solve(node.right, node.val, max_val)
    return left_subtree and right_subtree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return recursive_solve(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    test_tree = TreeNode(5)
    test_tree.left = TreeNode(1)
    test_tree.right = TreeNode(4)
    test_tree.right.right = TreeNode(6)
    test_tree.right.left = TreeNode(3)

    res = Solution().isValidBST(test_tree)
    print(res)