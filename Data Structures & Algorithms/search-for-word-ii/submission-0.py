class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:  # Fixed: was self.children
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, path):
            # 1. Base cases: out of bounds, already visited in this path, or char not in Trie
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visited or 
                board[r][c] not in node.children):
                return

            # 2. Mark as visited for this current path
            visited.add((r, c))
            node = node.children[board[r][c]]
            path += board[r][c]

            # 3. If we hit a valid word end, save it
            if node.end:
                res.add(path)

            # 4. Explore all 4 directions
            dfs(r + 1, c, node, path)
            dfs(r - 1, c, node, path)
            dfs(r, c + 1, node, path)
            dfs(r, c - 1, node, path)

            # 5. BACKTRACK: Un-mark the cell so other paths can use it!
            visited.remove((r, c))

        # Start DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root, "")

        return list(res)