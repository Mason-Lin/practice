# Build a trie
# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}


def fn(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want
    return root


# 208. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 211. Design Add and Search Words Data Structure
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def dfs(self, node, word, index):
        if index == len(word):
            return node.word
        if word[index] == ".":
            return any(self.dfs(child, word, index + 1) for child in node.children.values())
        node = node.children.get(word[index])
        if not node:
            return False
        return self.dfs(node, word, index + 1)

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)


def test_211():
    w = WordDictionary()
    w.addWord("bad")
    w.addWord("dad")
    w.addWord("mad")
    assert w.search("pad") is False
    assert w.search("bad") is True
    assert w.search(".ad") is True
    assert w.search("b..") is True
