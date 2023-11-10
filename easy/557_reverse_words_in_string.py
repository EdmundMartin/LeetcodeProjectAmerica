

def reverse_word(word: str):
    word_list = list(word)
    idx = 0
    while idx < len(word) / 2:
        word_list[idx], word_list[-(idx + 1)] = word_list[-(idx+1)], word_list[idx]
        idx += 1
    return "".join(word_list)


class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split(" "):
            result.append(reverse_word(word))
        return " ".join(result)


if __name__ == '__main__':
    res = reverse_word("Let's")
    print(res)