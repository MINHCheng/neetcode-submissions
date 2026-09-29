class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.trie
        def dfs(node, l):
            if l > len(word)-1 and node.end == True:
                return True
            elif l > len(word)-1:
                return False
            elif word[l] in node.children:
                node = node.children[word[l]]
                l +=1
                return dfs(node, l)
            elif word[l] == '.':
                l += 1
                for c in node.children:
                    if dfs(node.children[c], l):
                        return True
                return False
            else:
                return False

        return dfs(curr, 0)