from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:

        idx = 0
        parts = []
        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == "#":
                parts.append(s[idx:idx+2])
                idx += 3
            else:
                parts.append(s[idx])
                idx += 1
        result = ""
        for num in parts:
            result += ascii_lowercase[int(num)-1]
        return result



if __name__ == '__main__':
    res = Solution().freqAlphabets("10#11#12")
    print(res)

    res = Solution().freqAlphabets("1326#")
    print(res)