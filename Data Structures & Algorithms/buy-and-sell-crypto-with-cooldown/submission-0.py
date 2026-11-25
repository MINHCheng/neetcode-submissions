class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(i, coin):
            if i >= len(prices):
                return 0

            if (i,coin) in cache:
                return cache[(i,coin)]

            skip = dfs(i+1, coin)

            if coin:
                cache[(i, coin)] = max(dfs(i+2, 0) + prices[i], skip)     
            else:
                cache[(i, coin)] = max(dfs(i+1, 1)-prices[i], skip)

            return cache[(i,coin)]
        return dfs(0, 0)