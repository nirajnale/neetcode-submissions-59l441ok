class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.end

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)