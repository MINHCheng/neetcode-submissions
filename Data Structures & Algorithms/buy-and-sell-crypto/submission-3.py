class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        if len(prices) < 2:
            return 0

        profit = 0

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            
            if current_profit > 0:
                profit = max(profit, current_profit)
            else:
                left = right
            right +=1     


        return profit
        