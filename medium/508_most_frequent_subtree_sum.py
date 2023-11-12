from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solution(node: TreeNode, counter):
    if node is None:
        return 0
    subtree_left = recursive_solution(node.left, counter)
    subtree_right = recursive_solution(node.right, counter)
    total = node.val + subtree_left + subtree_right
    counter[total] += 1
    return total


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        recursive_solution(root, counter)
        most_frequent = max(counter.values())
        result = []
        for k, v in counter.items():
            if v == most_frequent:
                result.append(k)
        return result



if __name__ == '__main__':
    test_root = TreeNode(5)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(-3)

    Solution().findFrequentTreeSum(test_root)