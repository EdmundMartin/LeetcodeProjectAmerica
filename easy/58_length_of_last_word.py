

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = s.split(" ")
        word_size = 0
        for word in words:
            if len(word) > 0:
                word_size = len(word)
        return word_size


if __name__ == '__main__':
    Solution().lengthOfLastWord("   fly me   to   the moon  ")