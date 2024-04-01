from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.balanced = True

    def recursive_solve(self, node: TreeNode, depth: int) -> int:
        if node is None:
            return depth
        if node.left is not None:
            left = self.recursive_solve(node.left, depth + 1)
        else:
            left = depth

        if node.right is not None:
            right = self.recursive_solve(node.right, depth + 1)
        else:
            right = depth

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.recursive_solve(root, 0)
        return self.balanced


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)


    res = Solution().isBalanced(root)
    print(res)