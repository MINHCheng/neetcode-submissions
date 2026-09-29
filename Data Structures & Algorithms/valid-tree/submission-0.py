class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        visited = set()

        adj = {i:[] for i in range(n)}
        for p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)

        def dfs(curr, prev):            
            if curr in visited:
                return False
            
            visited.add(curr)
                    
            for c in adj[curr]:
                if c == prev:
                    continue
                if not dfs(c, curr):
                    return False
            return True
        
        return dfs(0,-1) and len(visited)==n
            


        