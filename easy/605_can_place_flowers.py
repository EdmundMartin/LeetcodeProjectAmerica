from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 1:
                continue
            plant_left = False
            if idx > 0:
                plant_left = flowerbed[idx - 1] == 1
            plant_right = False
            if idx < len(flowerbed) - 1:
                plant_right = flowerbed[idx + 1] == 1
            if plant_left or plant_right:
                continue
            flowerbed[idx] = 1
            n -= 1
            if n == 0:
                return True
        return n <= 0


if __name__ == '__main__':
    """
    res = Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(res)
    """

    res = Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print(res)