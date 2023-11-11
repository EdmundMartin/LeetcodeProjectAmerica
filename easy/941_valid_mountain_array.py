from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = max(arr)
        seen_peak = False

        if arr[-1] == peak:
            return False

        prev = float('-inf')
        for num in arr:
            if not seen_peak:
                if num <= prev:
                    return False
            if seen_peak:
                if num >= prev:
                    return False
            if num == peak:
                seen_peak = True
            prev = num
        return True


if __name__ == '__main__':
    res = Solution().validMountainArray([0, 3, 2, 1])
    print(res)

    res = Solution().validMountainArray([3, 5, 5])
    print(res)