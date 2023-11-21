from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_index(nums: List[int]):
    max_float = float('-inf')
    big_idx = -1
    for idx, num in enumerate(nums):
        if num > max_float:
            big_idx = idx
            max_float = num
    return big_idx


def recursive_solve(nums: List[int]):
    if len(nums) == 0:
        return
    idx = max_index(nums)

    node = TreeNode(nums[idx])
    node.left = recursive_solve(nums[:idx])
    node.right = recursive_solve(nums[idx+1:])
    return node


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return recursive_solve(nums)


if __name__ == '__main__':
    res = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])

