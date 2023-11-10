

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        res = arrivalTime + delayedTime
        return res % 24


if __name__ == '__main__':
    res = Solution().findDelayedArrivalTime(15, 5)
    print(res)

    res = Solution().findDelayedArrivalTime(13, 11)
    print(res)