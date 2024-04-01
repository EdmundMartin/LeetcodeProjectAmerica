from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            biggest_stones = [(-1, -1), (-1, -1)]
            for idx, stone in enumerate(stones):
                if stone > biggest_stones[-1][0]:
                    biggest_stones[0], biggest_stones[1] = biggest_stones[1], biggest_stones[0]
                    biggest_stones[-1] = [stone, idx]
                    continue
                if stone > biggest_stones[0][0]:
                    biggest_stones[0] = [stone, idx]
                    continue

            if biggest_stones[0] == biggest_stones[1]:
                idx_to_remove = sorted([
                    biggest_stones[0][1], biggest_stones[1][1]
                ], reverse=True)
                for idx in idx_to_remove:
                    stones.remove(idx)
            else:
                stone, idx = biggest_stones[-1]
                other, other_idx = biggest_stones[0]
                stones[idx] = stone - other
                stones.pop(other_idx)
        return sum(stones)




if __name__ == '__main__':
    Solution().lastStoneWeight([2, 7, 4, 8, 1])