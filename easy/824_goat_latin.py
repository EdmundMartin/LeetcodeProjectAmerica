

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")

        vowels = {'a', 'e', 'i', 'o', 'u'}

        goat_words = []
        for idx, word in enumerate(words):
            if word[0].lower() in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word = goat_word + ("a" * (idx + 1))
            goat_words.append(goat_word)
        return " ".join(goat_words)
