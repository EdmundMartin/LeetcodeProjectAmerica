from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        last_num = None

        highest_count = 0
        for num in nums:
            if num != last_num and last_num == 1:
                highest_count = max(count, highest_count)
                count = 1
            elif num != last_num:
                count = 1
            else:
                count += 1
            last_num = num
        if count > 0 and last_num == 1:
            highest_count = max(count, highest_count)
        return highest_count


if __name__ == '__main__':
    res = Solution().findMaxConsecutiveOnes([0, 1])
    print(res)

    res = Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
    print(res)

    res = Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])
    print(res)