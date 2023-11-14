

class Solution:
    def sortSentence(self, s: str) -> str:
        result = []
        for word in s.split(" "):
            w, idx = word[:-1], int(word[-1])
            result.append((idx, w))
        result = sorted(result)
        return ' '.join([
            x[1] for x in result
        ])


if __name__ == '__main__':
    res = Solution().sortSentence("is2 sentence4 This1 a3")
    print(res)