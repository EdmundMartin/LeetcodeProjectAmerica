from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        idx = 0
        seen = set()
        for ch in key:
            if ch.isalpha() and ch not in seen:
                mapping[ch] = ascii_lowercase[idx]
                idx += 1
                seen.add(ch)
        result = ""
        for ch in message:
            if ch == " ":
                result += ch
            else:
                result += mapping[ch]
        return result


if __name__ == '__main__':
    res = Solution().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
    print(res)