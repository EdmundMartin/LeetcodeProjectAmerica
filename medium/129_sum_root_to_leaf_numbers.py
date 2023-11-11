from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def number_list_to_num(nums: List[int]):
    total = 0
    multiplier = 0
    while nums:
        current_num = nums.pop(-1)
        if multiplier == 0:
            multiplier = 10
            total += current_num
            continue
        total += current_num * multiplier
        multiplier *= 10
    return total


def solve_recursively(node: TreeNode, current_path, results):
    if node is None:
        return
    if node.left is None and node.right is None:
        current_path.append(node.val)
        results.append(current_path)
        return
    current_path.append(node.val)
    solve_recursively(node.left, current_path[:], results)
    solve_recursively(node.right, current_path[:], results)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        solve_recursively(root, [], paths)
        return sum([
            number_list_to_num(n) for n in paths
        ])



if __name__ == '__main__':
    result = number_list_to_num([4, 2, 9])
    print(result)