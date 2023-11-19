

class Solution:
    def generateTheString(self, n: int) -> str:

        result = ""
        if n % 2 == 0:
            result += "".join(["a" * (n - 1)])
            result += "b"
            return result
        return "a" * n


if __name__ == '__main__':
    res = Solution().generateTheString(4)
    print(res)