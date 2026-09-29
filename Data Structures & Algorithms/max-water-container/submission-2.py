class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = 0
        l, r = 0, len(heights)-1

        while(l < r):
            size = min(heights[l],heights[r]) * (r-l)
            h = max(h, size)
            if(heights[l] >= heights[r]):
                r-=1
            else:
                l+=1
        return h
