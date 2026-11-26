class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {}
        for c1, c2 in prerequisites:
            pre.setdefault(c1, []).append(c2)
        
        visited = set()
        result = []
        for n in range(numCourses):
            if n not in pre:
                result.append(n)
        
        def dfs(node):
            if node in visited:
                return False
            if node in result:
                return True
            
            visited.add(node)
            for p in pre[node]:
                if not dfs(p):
                    return False
            visited.remove(node)

            result.append(node)
            return True
        
        for p in pre:
            if not dfs(p):
                return []
        return result

