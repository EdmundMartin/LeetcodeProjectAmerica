from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [None] * (len(nums) + 1)

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for key, value in counts.items():
            if buckets[value] is None:
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        result = []
        for r in buckets[::-1]:
            if r is not None:
                result.extend(r)
            if len(result) == k:
                return result


if __name__ == '__main__':
    Solution().topKFrequent([1, 1, 1, 2, 2, 100], 2)