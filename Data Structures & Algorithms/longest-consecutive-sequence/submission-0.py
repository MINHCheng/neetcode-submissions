class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        long : int = 0

        for num in numSet:
            if num-1 not in numSet:
                length = 1
                start = num
                while(start+1 in numSet):
                    length+=1
                    start+=1
                long=max(length, long)
        return long