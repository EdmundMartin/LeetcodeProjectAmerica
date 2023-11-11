from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.paths = []

    def recursive_solve(self, node: TreeNode, current_path: str):
        if node is None:
            return
        if node.left is None and node.right is None:
            current_path += str(node.val)
            self.paths.append(current_path)
            return
        path = current_path + f"{node.val}->"
        self.recursive_solve(node.left, path)
        self.recursive_solve(node.right, path)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.recursive_solve(root, "")
        return self.paths