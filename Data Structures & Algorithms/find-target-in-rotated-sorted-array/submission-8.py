class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # which side are we on, mid,right side check 
        l, r, m = 0, len(nums)-1, 0

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    print(f"1 {l}{r}")
                    r = m - 1
                else:
                    print(f"2 {l}{r}")
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    print(f"3 {l}{r}")
                    l = m + 1
                else:
                    print(f"4 {l}{r}")
                    r = m - 1
        return -1 
