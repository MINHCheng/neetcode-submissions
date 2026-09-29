class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        visited = set()
        graphs = 0
        def dfs(curr, prev):
            if not adj[curr]:
                return 
            visited.add(curr)
            
            for a in adj[curr]:
                if curr == prev :
                    continue
                if a not in visited:
                    dfs(a, curr)
            return
        
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                graphs += 1
        return graphs
            