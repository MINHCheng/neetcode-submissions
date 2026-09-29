class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxA = 0
        left = 0
        right = n-1
        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            maxA = max(maxA, width * h)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1 
        return maxA