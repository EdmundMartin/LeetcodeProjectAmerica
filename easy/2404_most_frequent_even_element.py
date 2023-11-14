from typing import List

from collections import defaultdict


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_value = float('-inf')
        max_key = None
        for num in nums:
            if num % 2 == 0 or num == 0:
                counter[num] += 1
                if counter[num] > max_value:
                    max_key = num
                    max_value = counter[num]
                elif counter[num] == max_value:
                    if max_key is None or num < max_key:
                        max_key = num
                        max_value = counter[num]
        return max_key if max_key is not None else -1