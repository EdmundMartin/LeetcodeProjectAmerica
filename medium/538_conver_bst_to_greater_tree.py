

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

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive_solve(root)
        return root