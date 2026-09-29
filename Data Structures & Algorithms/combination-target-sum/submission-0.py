class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        used = []
        def dfs(total, idx):
            if total > target or idx >= len(nums):
                return None
            if total == target:
                res.append(list(used))

            for i in range(idx, len(nums)):
                used.append(nums[i])
                dfs(total+nums[i], i)
                used.pop()


        dfs(0,0)
        return res