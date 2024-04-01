

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        current = 0
        while time > 0:
            if current == 0 or current == n - 1:
                direction *= -1
            current += direction
            time -= 1
        return current + 1


if __name__ == '__main__':
    res = Solution().passThePillow(8, 9)
    print(res)