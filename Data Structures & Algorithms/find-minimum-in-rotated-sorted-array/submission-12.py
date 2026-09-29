class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = nums[0]
        while(l <= r):
            if(nums[l] < nums[r]):
                res = min(res, nums[l])
                break
            
            m = l + (r-l)//2
            res = min(nums[m], res)

            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return res
        