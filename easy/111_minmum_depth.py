from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.max = float('inf')
        if root is None:
            return 0

        def recursive_solve(node: TreeNode, depth: int):
            if node.left is None and node.right is None:
                self.max = min(self.max, depth + 1)
            if node.left:
                recursive_solve(node.left, depth + 1)
            if node.right:
                recursive_solve(node.right, depth + 1)

        recursive_solve(root, 0)
        return self.max


if __name__ == '__main__':
    root_test = TreeNode(2)
    root_test.right = TreeNode(3)
    root_test.right.right = TreeNode(4)
    root_test.right.right.right = TreeNode(5)
    root_test.right.right.right = TreeNode(6)

    res = Solution().minDepth(root_test)
    print(res)

    root_test = TreeNode(3)
    root_test.left = TreeNode(9)

    res = Solution().minDepth(root_test)
    print(res)