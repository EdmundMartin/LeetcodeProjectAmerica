

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.value = 0

    def recursive_solve(self, node: TreeNode):
        if node is None:
            return
        self.recursive_solve(node.right)
        self.value = self.value + node.val
        node.val = self.value
        self.recursive_solve(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.recursive_solve(root)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    root.right.left = TreeNode(5)


    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)

    Solution().bstToGst(root)