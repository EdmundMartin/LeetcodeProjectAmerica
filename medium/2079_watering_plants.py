from typing import List


# 47ms - Beats 92.08% of users with Python3
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        if len(plants) == 0:
            return 0

        initial_capacity = capacity
        total_cost = 0
        for idx in range(len(plants)):

            if initial_capacity < plants[idx]:
                total_cost += idx + 1 + idx
                initial_capacity = capacity
                initial_capacity -= plants[idx]
            else:
                total_cost += 1
                initial_capacity -= plants[idx]
        return total_cost


if __name__ == '__main__':
    res = Solution().wateringPlants([2, 2, 3, 3], 5)
    print(res)

    res = Solution().wateringPlants([1, 1, 1, 4, 2, 3], 4)
    print(res)

    res = Solution().wateringPlants([7,7,7,7,7,7,7], 8)
    print(res)
