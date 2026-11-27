class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = [False]*len(nums)
        temp = []
        res = []
        def dfs():
            if len(temp)==len(nums):
                res.append(temp[:])
                return 
            for c in range(len(chosen)):
                if not chosen[c]:
                    chosen[c] = True
                    temp.append(nums[c])
                    dfs()
                    temp.pop()
                    chosen[c]=False
        dfs()
        return res