from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = [
            0 for _ in range(1, len(nums) + 1)
        ]
        results = set()
        for num in nums:
            idx = num - 1
            counts[idx] += 1
            if counts[idx] > 1:
                results.add(num)
        return list(results)



if __name__ == '__main__':
    res = Solution().findDuplicates([4,3,2,7,8,2,3,1])