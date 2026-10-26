class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        goal = len(cost)
        cost.append(0)
        cache = [None] * goal

        def dfs(i):
            if i >= goal:
                return 0
            if cache[i] is not None:
              return cache[i] 
            if i == goal:
                return cost[i]
            else:
                cache[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i+2))
            return cache[i]
        dfs(0)
        return min(cache[0], cache[1])