class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for n in range(len(nums)):
            if n not in nums:
                return n
        return nums[n]+1