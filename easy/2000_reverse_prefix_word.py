

def reverse_word(word: str):
    idx = 0
    word_list = list(word)
    while idx < len(word) // 2:
        word_list[idx], word_list[-(idx + 1)] = word_list[-(idx+1)], word_list[idx]
        idx += 1
    return "".join(word_list)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        idx = 0
        while idx < len(word):
            if word[idx] == ch:
                break
            idx += 1
        if idx == len(word):
            return word
        prefix = word[:idx+1]
        suffix = word[idx+1:]
        return prefix + suffix



if __name__ == '__main__':
    Solution().reversePrefix("abcdefd", "d")