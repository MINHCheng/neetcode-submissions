class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod = 1
        mn_prod = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                mx_prod = 1
                mn_prod = 1
                continue

            tmp = mx_prod * n          
            mx_prod = max(tmp, mn_prod * n, n)
            mn_prod = min(tmp, mn_prod * n, n)
            res = max(res, mx_prod, n)
        return res
        