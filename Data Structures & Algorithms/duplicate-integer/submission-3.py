class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers : dict = {}
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num]=1
        for itr in numbers.values():
            if itr > 1:
                return True

        return False