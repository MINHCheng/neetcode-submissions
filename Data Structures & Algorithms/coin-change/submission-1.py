class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        if amount == 0:
            return 0
        def pump(i):
            if i >= amount:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = float('inf')

            for coin in coins:
                if i + coin <= amount:
                    cache[i] = min(1 + pump(i + coin), cache[i])
                    
            return cache[i]
        pump(0)
        if cache[0] == float('inf'):
            return -1
        else:
            return cache[0]