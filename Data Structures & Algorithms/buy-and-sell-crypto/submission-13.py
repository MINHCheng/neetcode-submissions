class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB = prices[0]
        maxS = 0

        for p in prices:
            maxS = max(maxS, p-minB)
            minB = min(p, minB)
        return maxS