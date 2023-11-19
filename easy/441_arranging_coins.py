


class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairwell_size = 1
        count_steps = 0
        while n >= stairwell_size:
            count_steps += 1
            n -= stairwell_size
            stairwell_size += 1
        return count_steps