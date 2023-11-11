

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        queue = [(original, cloned)]
        while queue:
            og, clone = queue.pop(0)
            if og is None:
                continue
            if og == target:
                return clone
            if og.left:
                queue.append((og.left, clone.left))
            if og.right:
                queue.append((og.right, clone.right))
        return None
