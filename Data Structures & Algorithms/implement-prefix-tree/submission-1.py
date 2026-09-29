from collections import defaultdict

class TrieNode:
    # Tells Python to skip the heavy __dict__ and use fixed slots for speed
    __slots__ = ('children', 'end')
    
    def __init__(self):
        # Automatically instantiates a new TrieNode when a character isn't found
        self.children = defaultdict(TrieNode)
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c] # Clean and lightning fast
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True