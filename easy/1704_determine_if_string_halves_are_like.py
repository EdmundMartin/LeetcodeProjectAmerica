

def count_vowels(contents: str) -> int:
    vowels = {
        "a", "e", "i", "o", "u"
    }
    return sum([
        1 if a.lower() in vowels else 0 for a in contents
    ])


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        middle = len(s) // 2
        one, two = s[:middle], s[middle:]
        return count_vowels(one) == count_vowels(two)


if __name__ == '__main__':
    Solution().halvesAreAlike("textbook")