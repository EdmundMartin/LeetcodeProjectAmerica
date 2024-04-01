from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        result = 0
        while left < right:
            current_height = min(height[left], height[right])
            total = current_height * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            result = max(total, result)
        return result


if __name__ == '__main__':
    Solution().maxArea([1,8,6,2,5,4,8,3,7])