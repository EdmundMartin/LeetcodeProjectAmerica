


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traverse(node: TreeNode, values):
    if node is None:
        return
    values.append(node.val)
    in_order_traverse(node.left, values)
    in_order_traverse(node.right, values)


def build_recursively(values):
    if len(values) == 0:
        return
    if len(values) == 1:
        return TreeNode(values[0])

    middle = len(values) // 2
    left = values[:middle]
    right = values[middle+1:]
    node = TreeNode(values[middle])
    node.left = build_recursively(left)
    node.right = build_recursively(right)
    return node


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        in_order_traverse(root, values)
        values.sort()
        return build_recursively(values)


if __name__ == '__main__':
    test_tree = TreeNode(2)
    test_tree.left = TreeNode(1)
    test_tree.right = TreeNode(3)

    Solution().balanceBST(test_tree)