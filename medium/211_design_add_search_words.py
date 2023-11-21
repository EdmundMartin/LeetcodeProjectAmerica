
class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end_char = "*"

    def addWord(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node[self.end_char] = "END"

    def search(self, word: str) -> bool:
        nodes = [self.trie]
        for char in word:
            new_nodes = []
            if char == ".":
                for node in nodes:
                    new_nodes.extend(
                        [node[k] for k in node.keys() if k != "*"]
                    )
            else:
                not_found = True
                for node in nodes:
                    if char in node:
                        new_nodes.append(node[char])
                        not_found = False
                if not_found:
                    return False
            nodes = new_nodes
        return any([self.end_char in n for n in nodes])


if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("pad")
    res = wd.search("bad")
    print(res)
    res = wd.search(".ad")
    print(res)
    res = wd.search("b..")
    print(res)

    res = wd.search("tad")
    print(res)