class Solution:
    def rob(self, nums: List[int]) -> int:
        income = {i : [-1, -1] for i in range(len(nums))}

        if len(nums) == 1: return nums[0]

        def dfs(house, flag):
            if house >= len(nums) or (flag and house == len(nums) - 1):
                return 0
            if income[house][flag] != -1:
                return income[house][flag]
            
            income[house][flag] = max(nums[house] + dfs(house + 2, flag)
            , dfs(house + 1, flag))
            return income[house][flag]

        return max(dfs(0, True), dfs(1, False))