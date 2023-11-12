

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        inc = n
        while True:
            if n % inc == 0 and n % 2 == 0:
                return n
            n += inc