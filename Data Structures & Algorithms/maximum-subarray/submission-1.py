class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        result = float('-inf')

        for n in nums:
            curr_max += n
            curr_max = max(n, curr_max)
            result = max(result, curr_max)
        return result