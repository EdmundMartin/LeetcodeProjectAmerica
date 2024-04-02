from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solve(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    middle = len(nums) // 2
    node = TreeNode(nums[middle])
    node.left = recursive_solve(nums[:middle])
    node.right = recursive_solve(nums[middle+1:])
    return node


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return recursive_solve(nums)