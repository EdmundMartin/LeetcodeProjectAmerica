

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 1

        queue = [(root.left, root.val), (root.right, root.val)]

        while queue:
            current_node, max_path = queue.pop(0)

            if current_node is None:
                continue
            if current_node.val >= max_path:
                count += 1
            queue.append(
                (current_node.left, max(current_node.val, max_path))
            )
            queue.append(
                (current_node.right, max(current_node.val, max_path))
            )
        return count


if __name__ == '__main__':
    root_node = TreeNode(3)
    root_node.left = TreeNode(1)
    root_node.left.left = TreeNode(3)
    root_node.right = TreeNode(4)
    root_node.right.right = TreeNode(5)
    root_node.right.left  = TreeNode(1)

    res = Solution().goodNodes(root_node)
    print(res)