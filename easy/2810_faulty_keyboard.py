

class Solution:
    def finalString(self, s: str) -> str:
        current_input = ""

        for ch in s:
            if ch == "i":
                current_input = current_input[::-1]
            else:
                current_input += ch
        return current_input


if __name__ == '__main__':
    res = Solution().finalString("string")
    print(res)

    res = Solution().finalString("poiinter")
    print(res)