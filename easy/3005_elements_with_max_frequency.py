from collections import defaultdict


# Beats 99.83% of users with Python3
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        current_items = set()
        current_max = -1
        for num in nums:
            counter[num] += 1
            if counter[num] > current_max:
                current_items = {num}
                current_max = counter[num]
            elif counter[num] == current_max:
                current_items.add(num)
        total = 0
        for i in current_items:
            total += counter[i]
        return total
