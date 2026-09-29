class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prev_map = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prev_map[crs].append(pre)

        visit_set = set()

        def dfs(i):
            if i in visit_set:
                return False

            if prev_map[i] == []:
                return True
        

            visit_set.add(i)

            for cr in prev_map[i]:
                if not dfs(cr):
                    return False

            visit_set.remove(i)
            prev_map[i] = []

            return True


        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        