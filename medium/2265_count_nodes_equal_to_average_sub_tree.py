from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursive_solve(self, node: TreeNode, total, children):
        if node is None:
            return 0, 0
        left_total, left_childs = self.recursive_solve(node.left, total, children)
        right_total, right_childs = self.recursive_solve(node.right, total, children)

        current_total = node.val + left_total + right_total
        current_val = left_childs + right_childs + 1
        avg = current_total // current_val
        if avg == node.val:
            self.count += 1
        return current_total, current_val

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.recursive_solve(root, 0, 0)
        return self.count


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)

    Solution().averageOfSubtree(root)