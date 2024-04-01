from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1
        seen = set()
        while left <= right:
            middle = right + left // 2
            if middle in seen:
                return False
            seen.add(middle)

            if target in matrix[middle]:
                return True

            middle_val = matrix[middle][-1]
            if middle_val < target:
                left = middle + 1
            else:
                right = middle - 1
        return False


if __name__ == '__main__':
    """
    res = Solution().searchMatrix([[1], [3], [5]], 4)
    print(res)

    res = Solution().searchMatrix([[1]], 0)
    print(res)
    """
    res = Solution().searchMatrix([[1], [3], [5]], 5)
    print(res)