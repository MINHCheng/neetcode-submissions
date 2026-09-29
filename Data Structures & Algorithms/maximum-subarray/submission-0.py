class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = float('-inf')
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum < nums[i]:
                l = i
                running_sum = nums[i]
            res = max(running_sum, res)
        return res
         

        