from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        largest_right = [0] * len(height)
        largest_left = [0] * len(height)

        largest = 0
        for idx in range(len(height) - 2, -1, -1):
            largest = max(height[idx + 1], largest)
            largest_right[idx] = largest

        largest = 0
        for idx in range(1, len(height)):
            largest = max(height[idx - 1], largest)
            largest_left[idx] = largest

        total = 0
        for idx, num in enumerate(height):

            if largest_right[idx] == 0 or largest_left[idx] == 0:
                continue
            max_side = min(largest_right[idx], largest_left[idx])
            current_trapped = max_side - num
            if current_trapped > 0:
                total += current_trapped
        return total


if __name__ == '__main__':
    Solution().trap([4, 2, 0, 3, 2, 5])