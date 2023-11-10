

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0

        idx = 0
        while idx < len(s):
            if idx == len(s) - 1:
                total += symbols[s[idx]]
            elif symbols[s[idx]] < symbols[s[idx + 1]]:
                total -= symbols[s[idx]]
            else:
                total += symbols[s[idx]]
            idx += 1
        return total


if __name__ == '__main__':

    res = Solution().romanToInt("MCMXCIV")
    print(res)