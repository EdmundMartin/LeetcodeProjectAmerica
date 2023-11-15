

# 117ms - Beats 92.16% of users with Python3
class Trie:

    def __init__(self):
        self.trie = {}
        self.end_symbol = "*"

    def insert(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            if char not in current_node:
                current_node[char] = dict()
            current_node = current_node[char]
        current_node["*"] = "END"

    def search(self, word: str) -> bool:
        current_node = self.trie
        for ch in word:
            current_node = current_node.get(ch)
            if not current_node:
                return False
        return "*" in current_node

    def startsWith(self, prefix: str) -> bool:
        current_node = self.trie
        for ch in prefix:
            current_node = current_node.get(ch)
            if not current_node:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.trie)
    result = trie.search("apple")
    print(result)

    result = trie.startsWith("app")
    print(result)
