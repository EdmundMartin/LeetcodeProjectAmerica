

def recurse(num1, num2, ops: int):
    if num1 == 0 or num2 == 0:
        return ops
    if num1 >= num2:
        return recurse(num1 - num2, num2, ops + 1)
    else:
        return recurse(num2 - num1, num1, ops + 1)


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return recurse(num1, num2, 0)



if __name__ == '__main__':
    res = Solution().countOperations(10, 10)
    print(res)