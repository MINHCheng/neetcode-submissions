class Solution:
    def rob(self, nums: List[int]) -> int:
        money = {i : 0 for i in range(len(nums))}

        def dfs(house):
            if house not in range(len(nums)): return 0

            if money[house]:
                return money[house]
            
            money[house] = nums[house] + max(dfs(house + 2), dfs(house + 3))
            return money[house]
        return max(dfs(0), dfs(1))