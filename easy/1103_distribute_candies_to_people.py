from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0] * num_people

        idx = 0
        n = 1
        while candies:
            actual_idx = idx % num_people
            candy_given = min(candies, n)
            candies -= candy_given
            output[actual_idx] += candy_given
            n += 1
            idx += 1
        return output


if __name__ == '__main__':
    Solution().distributeCandies(7, 4)
    Solution().distributeCandies(10, 3)