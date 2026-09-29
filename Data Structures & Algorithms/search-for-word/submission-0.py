class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word : str):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        ROW, COL = len(board), len(board[0])

        trie = TrieNode()
        trie.add(word)

        def dfs(node, r, c):
            if not (0 <= r < ROW) or not(0 <=c < COL) or board[r][c] not in node.children or (r,c) in visited:
                return False

            node = node.children[board[r][c]]
            
            if node.end:
                return True
                
            visited.append((r,c))

            found = (
                dfs(node, r + 1, c) or 
                dfs(node, r - 1, c) or 
                dfs(node, r, c + 1) or 
                dfs(node, r, c - 1)
            )

            # 6. BACKTRACK: Un-mark the cell so other paths can use it
            visited.remove((r, c))

            return found
            

            
        for r in range(ROW):
            for c in range(COL):
                if dfs(trie, r, c):
                    return True
        return False
        