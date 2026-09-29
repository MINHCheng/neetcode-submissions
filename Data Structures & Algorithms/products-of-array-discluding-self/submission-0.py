class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = 1, []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count.append(i)
            else:
                product *= nums[i]
        solution =[0]*len(nums)
        if(len(zero_count) == 1): 
            solution[zero_count[0]] = product
        elif (len(zero_count) == 0):
            for j in range(len(nums)):
                solution[j] = int(product/nums[j])
        return solution         