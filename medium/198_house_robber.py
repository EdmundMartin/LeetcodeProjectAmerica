from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        rob_one = 0
        rob_two = 0

        for num in nums:
            temp = max(num + rob_one, rob_two)
            rob_one = rob_two
            rob_two = temp
        return rob_two
