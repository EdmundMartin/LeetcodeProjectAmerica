from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(node: Optional[TreeNode], results):
    if node is None:
        return
    results[node.val] += 1
    recursive_solve(node.left, results)
    recursive_solve(node.right, results)


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        recursive_solve(root, counter)
        max_count = max(counter.values())
        ret = []
        for k, v in counter.items():
            if v == max_count:
                ret.append(k)
        return ret