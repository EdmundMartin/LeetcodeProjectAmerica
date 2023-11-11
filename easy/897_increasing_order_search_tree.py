


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recursive(node: TreeNode, nodes):
    if node is None:
        return
    recursive(node.left, nodes)
    if len(nodes) > 0:
        new_node = TreeNode(node.val)
        nodes[-1].right = new_node
        nodes.append(new_node)
    else:
        nodes.append(TreeNode(node.val))
    recursive(node.right, nodes)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        all_nodes = []
        recursive(root, all_nodes)
        return all_nodes[0]