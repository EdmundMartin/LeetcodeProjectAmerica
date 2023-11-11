from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.paths = []

    def recursive_solve(self, node: TreeNode, current_path: List[int], target: int):
        if node is None:
            return None
        if node.left is None and node.right is None:
            current_path.append(node.val)
            if sum(current_path) == target:
                self.paths.append(current_path)
            return
        copy_left = current_path[:]
        copy_left.append(node.val)

        copy_right = current_path[:]
        copy_right.append(node.val)
        self.recursive_solve(node.left, copy_left, target)
        self.recursive_solve(node.right, copy_right, target)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.recursive_solve(root, [], targetSum)
        return self.paths


if __name__ == '__main__':
    root_node = TreeNode(5)
    root_node.left = TreeNode(4)
    root_node.left.left = TreeNode(11)
    root_node.left.left.right = TreeNode(2)
    root_node.left.left.left = TreeNode(7)

    res = Solution().pathSum(root_node, 22)
    print(res)