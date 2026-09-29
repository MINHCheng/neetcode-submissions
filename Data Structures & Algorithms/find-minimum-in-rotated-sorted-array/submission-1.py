class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, mid = 0, len(nums)-1, int((len(nums)-1)/2)
        
        while(l<r):
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1   
            mid = int((l + r) / 2)
        return nums[mid]

        